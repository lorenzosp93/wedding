from io import BytesIO
from PIL import Image
from django.db import IntegrityError
from django.forms import ValidationError
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from shared.models import ContentString, THUMBNAIL_SIZE
from .models import Information, InformationWidget, Photo


class TestInfo(TestCase):
    @staticmethod
    def get_image_file(
        name:str='test.webp',
        ext:str='webp',
        size:tuple[int, int]=(720, 720),
        color:tuple[int, int, int]=(0, 0, 0)
    ) -> SimpleUploadedFile:
        file_obj = BytesIO()
        with Image.new("RGB", size=size, color=color) as img:
            img.save(file_obj, format=ext, quality=10, optimize=True)
        file_obj.seek(0)
        return SimpleUploadedFile(content=file_obj.read(), name=name)

    def setUp(self,) -> None:
        content = ContentString.objects.create(value='someContent')
        self.info = Information.objects.create(
            subject=content,
            content=content,
            audience=30,
            type=0,
        )
        self.content_json='{"start": [2022,12,15]}'
        self.info_widget = InformationWidget.objects.create(
            info=self.info,
            type=0,
            content=self.content_json,
        )

    def test_photo_thumbnail(self) -> None:
        self.photo = Photo.objects.create(
            type=0,
            picture=self.get_image_file(),
        )
        with Image.open(self.photo.thumbnail) as thumb:
            self.assertIsInstance(thumb, Image.Image)
            self.assertEqual(thumb.size, THUMBNAIL_SIZE)
    
    def test_info_widget(self) -> None:
        self.assertEqual(
            self.info_widget.get_content_dict(),
            { "start": [2022, 12, 15,] },
        )

    def test_info_widget_unique(self) -> None:
        with self.assertRaises(ValidationError):
            InformationWidget.objects.create(
                type=0,
                info=self.info,
                content=self.content_json
            )

    def test_info_widget_bad_json(self) -> None:
        bad_json_comma = '{"start": [123,456],}'
        bad_json_bracket = '{"start": [123,456]'
        bad_json_quotes = "{start: [123,456]}"
        with self.assertRaises(ValidationError):
            InformationWidget.objects.create(
                info=self.info,
                type=1,
                content=bad_json_bracket,
            )
        with self.assertRaises(ValidationError):
            InformationWidget.objects.create(
                info=self.info,
                type=1,
                content=bad_json_comma,
            )
        with self.assertRaises(ValidationError):
            InformationWidget.objects.create(
                info=self.info,
                type=1,
                content=bad_json_quotes,
            )

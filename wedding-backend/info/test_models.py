from unittest.mock import Mock, patch
from io import BytesIO
from PIL import Image
from django.forms import ValidationError
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from profile.models import Keys, Subscription, UserProfile
from shared.models import ContentString, THUMBNAIL_SIZE
from .models import Information, InformationWidget, Photo


class TestInfo(TestCase):
    @staticmethod
    def get_image_file(
        name: str = 'test.webp',
        ext: str = 'webp',
        size: tuple[int, int] = (720, 720),
        color: tuple[int, int, int] = (0, 0, 0)
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
            type=3,
        )
        self.content_json = '{"start": [2022,12,15]}'
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
            {"start": [2022, 12, 15,]},
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


class TestTriggersNotification(TestCase):
    def setUp(self) -> None:
        content = ContentString.objects.create(value='someContent')
        self.info = Information.objects.create(
            subject=content,
            content=content,
            audience=30,
            type=3,
        )
        self.user = get_user_model().objects.create(
            username='testuser'
        )
        UserProfile.objects.create(
            user=self.user,
        )
        keys = Keys.objects.create(
            p256dh='testKey',
            auth='testAuth'
        )
        self.sub = Subscription.objects.create(
            keys=keys,
            user=self.user,
            endpoint='https://test.com',
            user_agent='testUserAgent'
        )

    def test_get_subscriptions(self) -> None:
        keys2 = Keys.objects.create(
            p256dh='testKey2',
            auth='testAuth2'
        )
        sub2 = Subscription.objects.create(
            keys=keys2,
            user=self.user,
            endpoint='https://test.com',
            user_agent='testUserAgent2'
        )
        users = self.info.get_users()
        self.assertIn(self.user, users)
        subs = self.info.get_subscriptions(users)
        self.assertIn(self.sub, subs)
        self.assertIn(sub2, subs)

    def test_build_payload(self) -> None:
        payload = self.info.build_payload()
        self.assertIn(self.info.subject.value, payload.get('body'))
        self.assertIn('data', payload)
        self.assertIn(self.info.get_type_display(), payload['data']['url'])

    @patch('info.models.Information.send_notifications')
    def test_trigger_notifications_save(
        self, send_notifications: Mock
    ) -> None:
        self.info.submit = True
        self.info.save()
        send_notifications.assert_called_once()
        self.assertFalse(self.info.submit)

    @patch('wedding.tasks.send_notifications_for_subscriptions.delay')
    def test_send_notifications(self, task: Mock) -> None:
        self.info.submit = True
        self.info.save()
        task.assert_called_once()

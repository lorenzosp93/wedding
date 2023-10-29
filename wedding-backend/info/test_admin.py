
from io import BytesIO
from PIL import Image
from amqp import Message
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib import admin
from .admin import PhotoAdmin
from .models import Photo
from django.contrib.messages.storage.fallback import FallbackStorage


class PhotoAdminTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('admin:upload-photos')

        image = Image.new('RGB', (100, 100), 'red')
        image_file = BytesIO()
        image.save(image_file, 'jpeg')
        image_file.seek(0)

        self.photo = SimpleUploadedFile(
            name='test_photo.jpg',
            content=image_file.read(),
            content_type='image/jpeg'
        )
        self.text_file = SimpleUploadedFile(
            name='test.txt',
            content=b'This is not a photo',
            content_type='text/plain'
        )


    def test_upload_single_photo(self):
        photo_count = Photo.objects.count()
        request = self.factory.post(self.url, {'type': 0, 'photos': self.photo})
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = PhotoAdmin(Photo, admin.site).upload_photos(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Photo.objects.count(), photo_count + 1)


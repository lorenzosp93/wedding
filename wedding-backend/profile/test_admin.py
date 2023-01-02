import csv
from io import StringIO
from unittest.mock import Mock, patch
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.core.files.uploadedfile import UploadedFile
from .admin import (
    HEADERS,
    UserAdmin
)


class TestCsvProfileAdmin(TestCase):
    def setUp(self) -> None:
        content = [
            '',        # username
            'test@email.com',  # email
            'testFirstName',   # first_name
            'testLastName',    # last_name
            'es',              # language
            '2',               # plus
            '3',               # type
        ]
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow(HEADERS.keys())
        writer.writerow(content)
        buffer.seek(0)
        self.csv = buffer
        self.factory = RequestFactory()

    @patch('profile.admin.UserAdmin.create_users_from_csv')
    @patch('django.contrib.messages.add_message')
    def test_import_csv(self, add_message: Mock, create_users: Mock) -> None:
        request = self.factory.post(
            '/api/admin/auth/user/import-csv/',
        )
        request.FILES['csv_file'] = UploadedFile(
            file=self.csv, name='testFile.csv', size=self.csv.__sizeof__()
        )
        response = UserAdmin(get_user_model(), admin.site
                             ).import_csv(request)
        self.assertEqual(response.status_code, 302)
        add_message.assert_called_once_with(
            request,
            20, "Your csv file has been imported",
            extra_tags='', fail_silently=False,
        )
        create_users.assert_called_once()

    def test_create_users_from_csv(self) -> None:
        reader = UserAdmin.open_csv(self.csv)
        if reader:
            UserAdmin.create_users_from_csv(reader)
        user = get_user_model().objects.filter(
            username='test@email.com'
        ).first()
        self.assertIsInstance(user, get_user_model())
        if user:
            self.assertEqual(user.first_name, 'testFirstName')
            self.assertEqual(user.last_name, 'testLastName')
            self.assertEqual(user.profile.type, 3)

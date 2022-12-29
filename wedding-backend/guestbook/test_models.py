from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Entry

# Create your tests here.


class TestGuestbookModels(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='testUser'
        )
        self.entry = Entry.objects.create(
            user=self.user,
            text='some text',
        )

    def test_entry_creation(self) -> None:
        self.assertIsInstance(self.entry, Entry)

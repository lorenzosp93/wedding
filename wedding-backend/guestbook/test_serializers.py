from django.test import TestCase
from django.contrib.auth import get_user_model
from .serializers import EntrySerializer
from .models import Entry


class TestEntrySerializer(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='testuser',
            first_name='a',
            last_name='b',
        )
        self.entry = Entry.objects.create(
            user=self.user,
            text='someText',
        )
        self.serializer = EntrySerializer()

    def test_entry_serializer(self) -> None:
        repr = self.serializer.to_representation(self.entry)
        self.assertEqual(repr.get('user_fullname'), 'a b')
        self.assertIsInstance(repr, dict)

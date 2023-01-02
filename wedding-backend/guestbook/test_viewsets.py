from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from .viewsets import EntryViewset
from .models import Entry
from .serializers import EntrySerializer

# Create your tests here.


class TestGuestbookViewsets(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create(
            username='testUser',
        )
        self.other_user = get_user_model().objects.create(
            username='otherTestUser',
        )
        self.entry = Entry.objects.create(
            user=self.user,
            text='someText',
        )
        self.other_entry = Entry.objects.create(
            user=self.other_user,
            text='someOtherText',
        )

    def test_entry_viewset_queryset(self) -> None:
        request = self.factory.get(reverse('guestbook:entry-list'))
        force_authenticate(request, self.user)
        response = EntryViewset.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            EntrySerializer().to_representation(self.other_entry),
            response.data
        )

    def test_create_entry_viewset(self) -> None:
        text = 'some test text'
        request = self.factory.post(
            reverse('guestbook:entry-list'),
            {'text': text, }
        )
        force_authenticate(request, self.user)
        response = EntryViewset.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)

    def test_delete_entry_viewset(self) -> None:
        request = self.factory.delete(
            reverse('guestbook:entry-detail', [self.entry.uuid]),
        )
        force_authenticate(request, self.user)
        response = EntryViewset.as_view(
            {'delete': 'destroy'})(request, pk=self.entry.uuid)
        self.assertEqual(response.status_code, 204)

    def test_delete_fail_entry_other_user_viewset(self) -> None:
        request = self.factory.delete(
            reverse('guestbook:entry-detail', [self.entry.uuid]),
        )
        force_authenticate(request, self.other_user)
        response = EntryViewset.as_view(
            {'delete': 'destroy'})(request, pk=self.entry.uuid)
        self.assertEqual(response.status_code, 404)

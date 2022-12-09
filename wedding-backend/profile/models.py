"Define abstract models to be used in all apps"
from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from shared.models import Address, I18N, TimeStampable

USER_TYPES = (
    (2, 'family'),
    (3, 'friend'),
    (5, 'colleague'),
)  # index should be prime number!


class UserProfile(models.Model):
    "Model to extend the built-in Django user with additional fields"
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    language = models.CharField(
        choices=I18N,
        default='en',
        max_length=2,
    )
    type = models.IntegerField(
        choices=USER_TYPES,
        default=2,
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    plus = models.IntegerField(default=0)
    parent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='childs',
    )

    def setup_plus_one(self, first_name: str, last_name: str, email: str) -> tuple[Optional[User], bool]:
        if self.user.childs.count() < self.plus:  # type: ignore
            user, created = User.objects.get_or_create(
                username=email,
            )
            if created:
                self.setup_profile(first_name, last_name, email, user)
            return user, created
        return None, False

    def setup_profile(self, first_name: str, last_name: str, email: str, user: User) -> None:
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        profile = UserProfile.objects.create(
            user=user,
            language=self.language,
            type=self.type,
            parent=self.user
        )

    def __str__(self):
        return self.user.username


class Keys(models.Model):
    p256dh = models.CharField(max_length=100)
    auth = models.CharField(max_length=30)


class Subscription(TimeStampable):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    endpoint = models.URLField()
    keys = models.OneToOneField(Keys, on_delete=models.CASCADE, null=True)

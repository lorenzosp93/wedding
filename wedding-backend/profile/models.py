"Define abstract models to be used in all apps"
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from shared.models import I18N, TimeStampable
from wedding.settings import AUTH_USER_MODEL

USER_TYPES = (
    (2, 'family'),
    (3, 'friend'),
    (5, 'colleague'),
)  # index should be prime number!


class UserProfile(models.Model):
    "Model to extend the built-in Django user with additional fields"
    user: models.Field = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    language: models.Field = models.CharField(
        choices=I18N,
        default='en',
        max_length=2,
    )
    type: models.Field = models.IntegerField(
        choices=USER_TYPES,
        default=2,
    )
    plus: models.Field = models.IntegerField(default=0)
    parent: models.Field = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='childs',
    )

    def setup_plus_one(
        self, first_name: str, last_name: str, email: str
    ) -> tuple[User | None, bool]:
        if self.user.childs.count() < self.plus:
            user, created = get_user_model().objects.get_or_create(
                username=email,
            )
            if created:
                self.setup_profile(first_name, last_name,
                                   email, user)
            return user, created
        return None, False

    def setup_profile(
        self, first_name: str, last_name: str, email: str, user: User
    ) -> None:
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        UserProfile.objects.create(
            user=user,
            language=self.language,
            type=self.type,
            parent=self.user
        )

    def __str__(self) -> str:
        return self.user.username


class Keys(models.Model):
    p256dh: models.Field = models.CharField(max_length=100)
    auth: models.Field = models.CharField(max_length=30)


class Subscription(TimeStampable):
    user: models.Field = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE)
    endpoint: models.Field = models.URLField()
    keys: models.Field = models.OneToOneField(
        Keys, on_delete=models.CASCADE, null=True)
    user_agent: models.Field = models.TextField()

    class Meta:
        unique_together = ['user', 'user_agent', 'endpoint']

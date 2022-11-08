"Define abstract models to be used in all apps"
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from shared.models import Address, I18N

USER_TYPES = (
    (0, 'family'),
    (1, 'friend'),
    (2, 'colleague'),
)

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
        default=0,
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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def setup_plus_one(self, first_name, last_name, email):
        if self.user.childs.count() < self.plus:
            user, created = User.objects.get_or_create(
                username=email,
            )
            if created:
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                profile = user.profile
                profile.language = self.language
                profile.type = self.type
                profile.parent = self.user
                profile.save()
            return user, created
        return None, False

    def __str__(self):
        return self.user.username
    
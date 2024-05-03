from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class User(AbstractUser):
    pass


@receiver(post_save, sender=User)
def add_to_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Пользователь')
        instance.groups.add(group)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from myreddit.settings import DEFAULT_USER_IMAGE


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name='Фото', default=DEFAULT_USER_IMAGE)
    status = models.CharField(max_length=80, default='', blank=True, null=True, verbose_name='Статус')
    groups = models.ManyToManyField('main.Group', blank=True, related_name='groups', verbose_name='Группы')
    likes = models.ManyToManyField('main.Post', blank=True, related_name='liked', verbose_name='Лайки')
    
    def get_absolute_url(self):
        return reverse("users:profile", kwargs={'pk': self.id})

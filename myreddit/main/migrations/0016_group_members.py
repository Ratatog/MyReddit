# Generated by Django 5.1.1 on 2024-09-20 09:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_comment_post_alter_group_admin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='member', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]

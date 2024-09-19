# Generated by Django 5.1.1 on 2024-09-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_img_image_url'),
        ('users', '0002_user_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='/media/users/avatar_default.png', null=True, upload_to='users/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked', to='main.post', verbose_name='Лайки'),
        ),
    ]

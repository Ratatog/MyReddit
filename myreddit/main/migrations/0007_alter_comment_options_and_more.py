# Generated by Django 5.1.1 on 2024-09-16 22:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comment_create_date_alter_comment_post_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_date']},
        ),
        migrations.RemoveIndex(
            model_name='post',
            name='main_post_text_b9eee0_idx',
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-likes'], name='main_commen_likes_1aca9c_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['text', '-likes', 'group', '-create_date'], name='main_post_text_cb3b81_idx'),
        ),
    ]

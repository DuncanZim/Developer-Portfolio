# Generated by Django 2.2.4 on 2019-08-06 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_picture',
        ),
    ]
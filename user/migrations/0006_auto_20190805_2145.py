# Generated by Django 2.2.4 on 2019-08-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190805_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_level',
            field=models.IntegerField(default=0),
        ),
    ]

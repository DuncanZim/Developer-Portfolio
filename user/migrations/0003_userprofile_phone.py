# Generated by Django 2.2.4 on 2019-08-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190805_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=27640506930, max_length=15),
        ),
    ]

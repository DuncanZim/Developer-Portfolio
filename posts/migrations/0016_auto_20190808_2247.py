# Generated by Django 2.2.4 on 2019-08-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20190808_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
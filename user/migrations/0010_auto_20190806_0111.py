# Generated by Django 2.2.4 on 2019-08-05 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190806_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='job_icon',
            new_name='category_icon',
        ),
    ]
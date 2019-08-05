# Generated by Django 2.2.4 on 2019-08-05 22:59

from django.db import migrations, models
import faicon.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190806_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('job_icon', faicon.fields.FAIconField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_icon',
        ),
    ]

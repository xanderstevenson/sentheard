# Generated by Django 3.0.8 on 2020-08-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200810_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='created_on',
        ),
        migrations.AddField(
            model_name='audio',
            name='description',
            field=models.TextField(default='', max_length=180),
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default='', max_length=180),
        ),
        migrations.AddField(
            model_name='text',
            name='description',
            field=models.TextField(default='', max_length=180),
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default='', max_length=180),
        ),
    ]

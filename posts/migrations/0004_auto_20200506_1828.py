# Generated by Django 3.0.4 on 2020-05-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200506_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]

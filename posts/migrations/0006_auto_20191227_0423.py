# Generated by Django 2.1 on 2019-12-27 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20191222_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(default='', upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='text',
            name='text_upload',
            field=models.FileField(default='', upload_to='text/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='', upload_to='video/'),
        ),
    ]
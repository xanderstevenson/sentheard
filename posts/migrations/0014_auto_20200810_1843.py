# Generated by Django 3.0.8 on 2020-08-10 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_photo_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='created_at',
            new_name='created_on',
        ),
    ]

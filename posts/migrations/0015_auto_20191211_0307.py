# Generated by Django 2.1 on 2019-12-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20191211_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='', upload_to='home/sentheard/sentheard/static/media/photos'),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20200811_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20200811_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_auto_20200812_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='description',
        ),
        migrations.AddField(
            model_name='text',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]

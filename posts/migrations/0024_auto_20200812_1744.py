# Generated by Django 3.0.8 on 2020-08-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20200812_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]

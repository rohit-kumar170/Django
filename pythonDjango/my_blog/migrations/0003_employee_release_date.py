# Generated by Django 4.2.7 on 2023-12-03 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='release_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

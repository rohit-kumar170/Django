# Generated by Django 4.2.7 on 2024-01-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_350,h_263,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/food-placeholder.jpg', max_length=500),
        ),
    ]

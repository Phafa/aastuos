# Generated by Django 5.0.3 on 2024-04-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]

# Generated by Django 5.0.4 on 2024-12-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_product_save'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='save',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

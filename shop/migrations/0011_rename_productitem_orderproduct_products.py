# Generated by Django 3.2.2 on 2022-03-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_orderproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='productItem',
            new_name='products',
        ),
    ]
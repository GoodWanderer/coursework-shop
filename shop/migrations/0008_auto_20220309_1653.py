# Generated by Django 3.2.2 on 2022-03-09 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_auto_20220309_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.CreateModel(
            name='Bascket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Стоимость (1 шт)')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bascketProduct', to='shop.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bascketUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
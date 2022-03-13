# Generated by Django 3.2.2 on 2022-03-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название слайда')),
                ('img', models.ImageField(upload_to='slider/', verbose_name='Изображение')),
                ('text', models.TextField(max_length=300, verbose_name='Текст на слайде')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1500, verbose_name='Описание'),
        ),
    ]

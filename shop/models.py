from django.db import models
import datetime 

# from accounts.models import UserAccount

class Contacts(models.Model):
  address = models.CharField(max_length=300, verbose_name='Адрес')
  phone = models.CharField(max_length=15, verbose_name='Телефон')
  email = models.EmailField(max_length=200, verbose_name='Почта')
  main = models.BooleanField(default=False, verbose_name='Главный офис?')

  class Meta:
    verbose_name = 'Контактные данные'
    verbose_name_plural = 'Контактные данные'

  def __str__(self):
    return 'Контактные данные'

class ContactsMe(models.Model):
  name = models.CharField(max_length=200, verbose_name='Имя')
  email = models.EmailField(max_length=200, verbose_name='Почта')
  phone = models.CharField(max_length=20, verbose_name='Телефон')
  message = models.TextField(max_length=3000, verbose_name='Сообшение')

  class Meta:
    verbose_name = 'Запрос обратной связи'
    verbose_name_plural = 'Запросы обратной связи'

  def __str__(self):
    return 'Запрос обратной связи'



class Faq(models.Model):
  question = models.TextField(max_length=350, verbose_name='Вопрос')
  answer = models.TextField(max_length=1000, verbose_name='Ответ')

  class Meta:
    verbose_name = 'Вопрос и ответ'
    verbose_name_plural = 'Вопросы и ответы'

  def __str__(self):
    return 'Вопрос и ответ'



class Category(models.Model):
  name = models.CharField(max_length=150, verbose_name='Название категории')
  slug = models.SlugField(verbose_name='Индификатор', unique=True)

  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

  def __str__(self):
    return self.name

class Product(models.Model):
  title = models.CharField(max_length=150, verbose_name='Название')
  img = models.ImageField(upload_to='products/', verbose_name='Изображение')
  stock = models.BooleanField(default=False, verbose_name='Акционный товар')
  price = models.IntegerField(verbose_name='Стоимость')
  available = models.BooleanField(default=True, verbose_name='В наличии?')
  model = models.CharField(max_length=150, verbose_name='Модель')
  company = models.CharField(max_length=150, verbose_name='Компания')
  description = models.TextField(max_length=1500, verbose_name='Описание')
  category = models.ForeignKey('category', on_delete=models.CASCADE, related_name='categoryProduct', verbose_name='Категория')

  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'

  def __str__(self):
    return self.title
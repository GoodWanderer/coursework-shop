from django.db import models
import datetime 

from accounts.models import UserAccount

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



class Slider(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название слайда')
  img = models.ImageField(upload_to='slider/', verbose_name='Изображение')
  text = models.TextField(max_length=300, verbose_name='Текст на слайде')

  class Meta:
    verbose_name = 'Слайд'
    verbose_name_plural = 'Слайды'

  def __str__(self):
    return 'Слайд - {}'.format(self.name)



class Basket(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='bascketUser', verbose_name='Пользователь')
  products = models.ForeignKey('product', on_delete=models.CASCADE, related_name='bascketProduct', verbose_name='Товар')
  price = models.IntegerField(verbose_name='Стоимость (1 шт)')
  quantity = models.IntegerField(verbose_name='Количество')

  class Meta:
    verbose_name = 'Корзина'
    verbose_name_plural = 'Корзина'

  def __str__(self):
    return 'Товар в корзине'


class Order(models.Model):
  key = models.CharField(max_length=100, unique=True, verbose_name="Номер заказа")
  user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='orderUser', verbose_name='Пользователь')
  totalSum = models.IntegerField(verbose_name='Общая сумма покупки')

  class Meta:
    verbose_name = 'Покупка'
    verbose_name_plural = 'Покупки'

  def __str__(self):
    return 'Заказ - {}'.format(self.key)

class OrderProduct(models.Model):
  order = models.ForeignKey('order', on_delete=models.CASCADE, related_name='orderItem', verbose_name='Покупка')
  product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orderProduct', verbose_name='Товар')
  price = models.IntegerField(verbose_name='Стоимость')
  quantity = models.IntegerField(verbose_name='Количество')
  totalSum = models.IntegerField(verbose_name='Сумма покупки')

  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Купленные тоары'

  def __str__(self):
    return 'Покупки'
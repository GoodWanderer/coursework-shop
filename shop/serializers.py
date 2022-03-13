from rest_framework import fields, serializers

from .models import Contacts, ContactsMe
from .models import Faq
from .models import Product, Category
from .models import Slider
from .models import Basket
from .models import Order, OrderProduct


class ContactsSerializer(serializers.ModelSerializer):
  class Meta:
      model = Contacts
      fields = '__all__'

class ContactsMeSerializer(serializers.ModelSerializer):
  class Meta:
      model = ContactsMe
      fields = ('__all__')



class FaqSerializer(serializers.ModelSerializer):
  class Meta:
      model = Faq
      fields = ('__all__')



class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('__all__')



class SliderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slider
    fields = ('__all__')


class BasketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Basket
    fields = ('__all__')

class OrderProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderProduct
    fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ('__all__')
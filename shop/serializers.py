from rest_framework import fields, serializers

from .models import Contacts, ContactsMe
from .models import Faq
from .models import Product, Category


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
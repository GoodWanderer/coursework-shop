from django.contrib import admin

admin.site.site_title = 'ShoeStore'
admin.site.site_header = 'ShoeStore'

from .models import Contacts, ContactsMe
from .models import Faq
from .models import Category, Product
from .models import Slider
from .models import Order, OrderProduct


class OrderProductInline(admin.TabularInline): 
  fk_name = 'order'
  model = OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('key', 'user', 'totalSum')
  inlines = [OrderProductInline,]

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'main')

@admin.register(ContactsMe)
class ContactsMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'available', 'company', 'model', 'stock')

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
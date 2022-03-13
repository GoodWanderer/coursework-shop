from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import UserAccount
from shop.models import Basket

admin.site.unregister(Group)

class BasketInline(admin.TabularInline): 
  fk_name = 'user'
  model = Basket

@admin.register(UserAccount)
class PromotionsAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (('Разрешения'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
  )
  inlines = [BasketInline,]
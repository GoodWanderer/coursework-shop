from django.urls import path

from .views import contacts_view, contacts_me_view
from .views import faq_view
from .views import сategory_and_stocks_view, products_view, products_view_for_сategory
from .views import slider_view
from .views import products_new_view
from .views import product_detail_view
from .views import product_search
from .views import basket_view, basket_add_view, basket_upadate_view, basket_del_view
from .views import order_view

urlpatterns = [
  
    path('contacts/', contacts_view, name=None),

    path('contacts-me/', contacts_me_view, name=None),
    path('faq/', faq_view, name=None),
    path('slider/', slider_view, name=None),

    path('сategory/', сategory_and_stocks_view, name=None),

    path('order/', order_view, name=None),

    path('basket/del/', basket_del_view, name=None),
    path('basket/upadate/', basket_upadate_view, name=None),
    path('basket/add/', basket_add_view, name=None),
    path('basket/<int:id>', basket_view, name=None),

    path('product/detail/<int:id>', product_detail_view, name=None),

    path('products/page/<int:qPage>', products_view, name=None),
    path('products/сategory/<slug:slug>', products_view_for_сategory, name=None),
    path('products/сategory/page/<slug:slug>/<int:qPage>', products_view_for_сategory, name=None),
    path('products/new/', products_new_view, name=None),
    path('products/', products_view, name=None),

    path('search/products/', product_search, name=None),
]


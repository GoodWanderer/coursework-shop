from django.core.paginator import Paginator

from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import Contacts, ContactsMe
from .serializers import ContactsSerializer, ContactsMeSerializer

from .models import Faq
from .serializers import FaqSerializer

from .models import Slider
from .serializers import SliderSerializer

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from .models import Basket
from .serializers import BasketSerializer

from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer



@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def contacts_view(request):
  try:
    contacts_list = Contacts.objects.all()
    serializers  = ContactsSerializer(contacts_list, many=True)
    return Response(serializers.data)
  except:
    return Response({"status": "server_error"})


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def contacts_me_view(request):
  try:
    # if request.method == "POST":
    data = request.data
    serializers = ContactsMeSerializer(data=data)
    
    if not serializers.is_valid():
      return Response({"status": "data_not_valid"})

    serializers.save()
    return Response({"status": "success"})
  except:
    return Response({"status": "server_error"})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def faq_view(request):
  try:
    faq_list = Faq.objects.all()
    serializers  = FaqSerializer(faq_list, many=True)
    return Response(serializers.data)
  except:
    return Response({"status": "server_error"})



@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def сategory_and_stocks_view(request):
  try:
    сategory_list = Category.objects.all()
    serializersC  = CategorySerializer(сategory_list, many=True)

    products_list = Product.objects.filter(stock=True)
    pagin = Paginator(products_list, 4)
    pagin_lsit = pagin.page(1)
    serializersP = ProductSerializer(pagin_lsit, many=True)
    return Response({"prod": serializersP.data, "cat": serializersC.data})
  except:
    print(8)
    return Response({"status": "server_error"})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def products_view(request, qPage = 1):
  try:
    products_list = Product.objects.all()
    
    pagin = Paginator(products_list, 6)
    pagin_lsit = pagin.page(qPage)


    serializers  = ProductSerializer(pagin_lsit, many=True)
    return Response({"data": serializers.data, "qPage":pagin.num_pages})
  except:
    return Response({"status": "server_error"})



@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def products_view_for_сategory(request, slug, qPage = 1):
  try:
    category = Category.objects.get(slug=slug)

    # products_list = Product.objects.filter(category=category.id)
    # serializers  = ProductSerializer(products_list, many=True)

    products_list = Product.objects.filter(category=category.id)
    
    pagin = Paginator(products_list, 6)
    pagin_lsit = pagin.page(qPage)

    serializers  = ProductSerializer(pagin_lsit, many=True)
    return Response({"data": serializers.data, "qPage":pagin.num_pages})

    # return Response({"data": serializers.data, "qPage":1})
  except:
    return Response({"status": "server_error"})



@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def product_detail_view(request, id):
  try:
    product = Product.objects.get(id=id)
    serializers  = ProductSerializer(product)

    products_sim_list = Product.objects.filter(category=product.category).exclude(id=id)
    pagin = Paginator(products_sim_list, 3)
    pagin_lsit = pagin.page(1)
    serializersSim  = ProductSerializer(pagin_lsit, many=True)
    return Response({"status": "success", "data": serializers.data, 'sim': serializersSim.data})
  except:
    return Response({"status": "server_error"})


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def product_search(request):
  try:
    title = request.data['title']
    qPage = request.data['qPage']
    products_list = Product.objects.filter(title__icontains=title)
    pagin = Paginator(products_list, 6)
    pagin_lsit = pagin.page(qPage)
    serializersSim  = ProductSerializer(pagin_lsit, many=True)
    return Response({"status": "success", "data": serializersSim.data, "qPage":pagin.num_pages})
  except:
    return Response({"status": "server_error"})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def products_new_view(request):
  try:
    products_list = Product.objects.all().order_by('-id')
    pagin = Paginator(products_list, 6)
    pagin_lsit = pagin.page(1)
    serializers = ProductSerializer(pagin_lsit, many=True)
    return Response({"status": "success", "data": serializers.data})
  except:
    return Response({"status": "server_error", "data": []})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def slider_view(request):
  try:
    slider_list = Slider.objects.all()
    serializers = SliderSerializer(slider_list, many=True)
    return Response(serializers.data)
  except:
    return Response({"status": "server_error", "data": []})


@api_view(['GET'])
@authentication_classes(())
@permission_classes(())
def basket_view(request, id):
  try:
    basket_list = Basket.objects.filter(user=id)
    serializers = BasketSerializer(basket_list, many=True)

    for serial in serializers.data:
      try:
        prod = Product.objects.get(id=serial['products'])
        serial['productName'] = prod.title
        serial['productImg'] = prod.img.url
      except:
        serial['productName'] = 'Данного товара не существет'
        serial['productImg'] = ''

    return Response({"status": "success", "data": serializers.data})
  except:
    return Response({"status": "server_error", "data": [], "quantity": 0})


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def basket_add_view(request):
  try:
    data = request.data
    serializers = BasketSerializer(data=data)
    
    if not serializers.is_valid():
      return Response({"status": "data_not_valid"})

    basket_product = Basket.objects.filter(user=data['user']).filter(products=data['products']).first()
    
    if not basket_product:
      serializers.save()
    else:
      basketSerializers = BasketSerializer(basket_product)

      basket_product.quantity = basket_product.quantity+ data['quantity']
      basket_product.save()

    return Response({"status": "success"})
  except:
    return Response({"status": "server_error"})


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def basket_upadate_view(request):
  try:
    data = request.data
    basket_products = Basket.objects.filter(user=data['user'])
    for product in basket_products:
      if product.id == data['products']:
        product.quantity = data['quantity']
        product.save()
    return Response({"status": "success"})
  except:
    return Response({"status": "server_error"})


@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def basket_del_view(request):
  try:
    data = request.data
    basket_products = Basket.objects.filter(user=data['user'])
    for product in basket_products:
      if product.id == data['products']:
        product.delete()
    return Response({"status": "success"})
  except:
    return Response({"status": "server_error"})


from uuid import uuid4

@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def order_view(request):
  try:
    data = request.data
    key = str(uuid4())
    order = {"key": key, "user": data['user'], "totalSum": 0}

    serializersOrder = OrderSerializer(data=order)

    if not serializersOrder.is_valid():
      return Response({"status": "data_not_valid"})

    serializersOrder.save()

    currentOrder = Order.objects.filter(key=key).first()
    basket_products = Basket.objects.filter(user=data['user'])
  
    allPrice = 0

    for basket_product in basket_products:
      product = Product.objects.filter(id=basket_product.products.id).first()

      orderItem = OrderProduct(
        order=currentOrder,
        product=product,
        price=product.price,
        quantity=basket_product.quantity,
        totalSum=product.price*basket_product.quantity
      )

      allPrice = allPrice + product.price*basket_product.quantity

      orderItem.save()
      basket_product.delete()
 
    currentOrder.totalSum = allPrice
    currentOrder.save()
    return Response({"status": "success"})
  except:
    print('error')
    return Response({"status": "server_error"})
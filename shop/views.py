from django.core.paginator import Paginator

from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import Contacts, ContactsMe
from .serializers import ContactsSerializer, ContactsMeSerializer

from .models import Faq
from .serializers import FaqSerializer

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer



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
    if request.method == "POST":
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
    print(title, qPage)
    products_list = Product.objects.filter(title__icontains=title)
    print(1)
    pagin = Paginator(products_list, 6)
    print(2)
    pagin_lsit = pagin.page(qPage)
    print(3)
    serializersSim  = ProductSerializer(pagin_lsit, many=True)
    print(4)
    return Response({"status": "success", "data": serializersSim.data, "qPage":pagin.num_pages})
  except:
    return Response({"status": "server_error"})
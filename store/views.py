import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import ProfileSerializer, ProductSerializer
from .models import Product
from rest_framework.pagination import PageNumberPagination
import stripe
from dotenv import load_dotenv
load_dotenv()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    category_name = request.GET.get('category')
    products = Product.objects.all()
    if category_name:
        products = products.filter(category__name__icontains=category_name)

    paginator = PageNumberPagination()
    paginator.page_size = 2
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    product_id = request.data.get('product_id')
    product = Product.objects.get(id=product_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(product.price * 100),
                'product_data': {
                    'name': product.title,
                },
            },
            'quantity': 1,
        }],
        mode='payment',

        success_url='http://127.0.0.1:8000/api/success/',
        cancel_url='http://127.0.0.1:8000/api/cancel/',
    )
    return Response({'checkout_url': session.url})


def payment_success(request):
    return HttpResponse("Payment successful!")

def payment_cancel(request):
    return HttpResponse("Payment canceled!")
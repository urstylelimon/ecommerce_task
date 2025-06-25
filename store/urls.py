
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import profile_view, product_list, create_checkout_session , payment_success,payment_cancel

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', profile_view),
    path('products/', product_list),
    path('checkout-session/', create_checkout_session),
    path('success/', payment_success),
    path('cancel/', payment_cancel),
]


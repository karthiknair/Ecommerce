from django.urls import path
from . views import Home, login_view
from Cart.views import add_to_cart, remove_from_cart,Cartv
app_name= 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    path('login', login_view, name='login'),
    path('cartview', Cartv.as_view(), name='cartv'),

]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('login',views.login.as_view(),name='login'),
    path('signup',views.signup.as_view(),name='signup'),
    path('productdetails/<int:pk>',views.ProductDeatils.as_view(),name='productdetails'),

    path('menswear',views.menswear,name='menswear'),
    path('womenswear',views.womenswear,name='womenswear'),
    path('accessories',views.accessories,name='accessories'),

    path('add_to_cart',views.add_to_cart,name='add_to_cart'), 
    path('cart',views.cart,name='cart'), 
    path('cart_delete/<int:id>',views.cart_delete,name='cart_delete'),

    path('logout',views.logout,name="logout"),
    path('address',views.address.as_view(),name='address'),
    path('order',views.order,name="order"),

    path('profile',views.profile,name="profile"),
    path('add_delete/<int:id>',views.add_delete,name='add_delete'),
    path('add_edit/<int:id>',views.add_edit,name='add_edit'),

    path('checkout',views.checkout.as_view(),name='checkout'),
    path('payment',views.payment.as_view(),name='payment'),
    path('ordersuccess',views.ordersuccess,name='ordersuccess'),

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)



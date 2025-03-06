from django.urls import path
from ecomwebsite.views import loginpage, dashboard_page, header_page, footer_page, signup_page, products_page, orders_page, users_page, checkout_page, ordersucess_page, base_page, logout_view, deals_view, home_view

urlpatterns = [

    path('',loginpage, name = "loginpage"),
    path('dashboard',dashboard_page, name = "dashboard"),
    path('header',header_page, name = "header"),
    path('footer',footer_page, name = "footer"),
    path('signup',signup_page, name = "signup"),
    path('products',products_page, name = "products"),
    path('orders',orders_page, name = "orders"),
    path('users', users_page, name = "user"),
    path('checkout',checkout_page, name = "checkout"),
    path('ordersucess',ordersucess_page, name = "ordersucess"),
    path('base', base_page, name = "base"),
    path('logout/', logout_view, name='logout_user'),
    path('deals/', deals_view, name='deals'),
    path('home', home_view, name='home'),    

         
]
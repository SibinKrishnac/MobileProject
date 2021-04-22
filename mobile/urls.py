"""MobileApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import create_brand,brand_delete,brand_update,create_mobile,list_mobiles,mobile_detail,user_registration,user_login,user_logout,order,cart,errorpg,cancel,view_order

urlpatterns = [
    path("",lambda request:render(request,"mobile/index.html")),
    path("brands",create_brand,name="brands"),
    path("brands/delete/<int:id>",brand_delete,name="delete"),
    path("brands/edit/<int:id>",brand_update,name="edit"),
    path("mobiles",create_mobile,name="createmobile"),
    path("mobiles/list",list_mobiles,name="listmobiles"),
    path("mobiles/detail/<int:id>",mobile_detail,name="detail"),
    path("mobiles/userRegistration",user_registration,name="register"),
    path("userlogin",user_login,name="userlogin"),
    path("userlogout",user_logout,name="userlogout"),
    path("mobiles/order/<int:id>",order,name="order"),
    path("mobiles/cart",cart,name="cart"),
    path("mobiles/error",errorpg,name="errorpg"),
    path("mobiles/cancel/<int:id>",cancel,name="cancel"),
    path("mobiles/vieworder/<int:id>",view_order,name="vieworder")
]
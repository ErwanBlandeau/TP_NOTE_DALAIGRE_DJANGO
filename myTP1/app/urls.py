"""
URL configuration for myTP1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import *
from . import views

urlpatterns = [
   
    # path("product/<pk>",views.ProductDetailView.as_view()),
    # path("home", views.home, name="home"),
    # path("product/add/",views.ProductCreate, name="product-add"),

    #Page quelcquonque
    path('home/', views.HomeView.as_view(), name='home_no_param'),  # Sans paramètre
    path('home/<param>/', views.HomeParamView.as_view(), name='home'),  # Avec paramètre
    path("contact", views.ContactView, name="contact"),
    path("about", views.AboutView.as_view(), name="about"),
    path('email_sent/', views.EmailSentView.as_view(), name='email-sent')   , 
    


    #Connexion
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    #Add
    path("product/add/",views.ProductCreateView.as_view(), name="product-add"),
    path("item/add/",views.ProductItemCreateView.as_view(), name="product-item-add"),
    path("attribute/add/",views.ProductAttributeCreateView.as_view(), name="product-attribute-add"),

    #Update
    path("attribute/<pk>/update/",views.ProductAttributeUpdateView.as_view(), name="product-attribute-update"),
    path("item/<pk>/update/",views.ProductItemUpdateView.as_view(), name="product-item-update"),
    path("product/<pk>/update/",views.ProductUpdateView.as_view(), name="product-update"),

    #Delete
    path("product/<pk>/delete/",views.ProductDeleteView.as_view(), name="product-delete"),
    path("item/<pk>/delete/",views.ProductItemDeleteView.as_view(), name="product-item-delete"),
    path("attribute/<pk>/delete/",views.ProductAttributeDeleteView.as_view(), name="product-attribute-delete"),

    # ListView
    path('product', views.ProductListView.as_view(), name="product-list"),
    path('item', views.ProductItemListView.as_view(), name="item-list"),
    path('attribute', views.ProductAttributeListView.as_view(), name="attribute-list"),

    #Detail
    path("product/<pk>",views.ProductDetailView.as_view(), name="product-detail"),
    path("attribute/<pk>",views.ProductAttributeDetailView.as_view(), name="attribute-detail"),


    #TP_NOTE


    # ListView
    path('fournisseur', views.FournisseurListView.as_view(), name="fournisseur-list"),

    #Add
    path("fournisseur/add/",views.FournisseurCreateView.as_view(), name="fournisseur-add"),
]

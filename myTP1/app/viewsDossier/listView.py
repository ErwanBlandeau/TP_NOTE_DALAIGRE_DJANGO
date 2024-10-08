from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail
from django.shortcuts import redirect
from app.forms import ContactUsForm, ProductAttributeForm, ProductForm, ProductItemForm
from django.forms import BaseModelForm
from ..models import Fournisseur, Product, ProductAttribute, ProductFournisseur, ProductItem

class ProductItemListView(ListView):
    model = ProductItem
    template_name = "affichage_total.html"
    context_object_name = "prdct"
    def get_queryset(self ):
        print(ProductItem.objects.select_related('product').prefetch_related('attributes'))
        return ProductItem.objects.select_related('product').prefetch_related('attributes')
    def get_context_data(self, **kwargs):
        context = super(ProductItemListView, self).get_context_data(**kwargs)
        context['titremenu'] = "item"
        return context
    
class ProductAttributeListView(ListView):
    model = ProductAttribute
    template_name = "affichage_total.html"
    context_object_name = "prdct"
    def get_queryset(self ):
        return ProductAttribute.objects.all().prefetch_related('productattributevalue_set')
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeListView, self).get_context_data(**kwargs)
        context['titremenu'] = "attribut"
        return context


#TP NOTEE



class ProductListView(ListView):
    model = Product
    template_name = "affichage_total.html"
    context_object_name = "prdct"

    def get_queryset(self ) :
        # return prdct.order_by("price_ttc")
        return Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['titremenu'] = "produits"
        return context
    
class FournisseurListView(ListView):
    model = Fournisseur
    template_name = "affichage_total.html"
    context_object_name = "prdct"

    def get_queryset(self ) :
        return Fournisseur.objects.all().order_by("name")
    
    def get_context_data(self, **kwargs):
        context = super(FournisseurListView, self).get_context_data(**kwargs)
        context['titremenu'] = "fournisseur"
        return context
    
class ProductFournisseurListView(ListView):
    model = Product
    template_name = "affichage_total.html"
    context_object_name = "prdct"

    def get_queryset(self ) :
        res = ProductFournisseur.objects.all().prefetch_related('product')
        print(res)
        return ProductFournisseur.objects.all().prefetch_related('product')
    
    def get_context_data(self, **kwargs):
        context = super(ProductFournisseurListView, self).get_context_data(**kwargs)
        context['titremenu'] = "produits Fournisseur"
        return context
    

    
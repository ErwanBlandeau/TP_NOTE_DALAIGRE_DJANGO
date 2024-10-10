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
from ..models import Product, ProductAttribute, ProductItem , Commande



# class ProductItemListView(ListView):
#     model = ProductItem
#     template_name = "affichage_total.html"
#     context_object_name = "prdct"

#     def get_queryset(self ) :
#         # return prdct.order_by("price_ttc")
#         return ProductItem.objects.all() 
    
#     def get_context_data(self, **kwargs):
#         context = super(ProductItemListView, self).get_context_data(**kwargs )
#         context['titremenu'] = "item"
#         return context

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

# class ProductAttributeListView(ListView):
#     model = ProductAttribute
#     template_name = "affichage_total.html"
#     context_object_name = "prdct"

#     def get_queryset(self ) :
#         # return prdct.order_by("price_ttc")
#         return ProductAttribute.objects.all()   
    
#     def get_context_data(self, **kwargs):
#         context = super(ProductAttributeListView, self).get_context_data(**kwargs )
#         context['titremenu'] = "attribut"
#         return context

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

class ProductListView(ListView):
    model = Product
    template_name = "affichage_total.html"
    context_object_name = "prdct"

    def get_queryset(self ) :
        # return prdct.order_by("price_ttc")
        return Product.objects.all().order_by("price_ttc")    
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['titremenu'] = "produits"
        return context
    
    
class CommandeListView(ListView):
    model = Commande
    template_name = "affichage_total.html"
    context_object_name = "prdct"

    def get_queryset(self ) :
        # return prdct.order_by("price_ttc")
        return Commande.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(CommandeListView, self).get_context_data(**kwargs)
        context['titremenu'] = "commande"
        return context

# def ListProducts(request):
#     prdcts = Product.objects.all()
#     return HttpResponse(f"""
#                 <p>Mes produits sont :<p>
#                 <ul>
#                 <li>{prdcts[0].name}</li>
#                 <li>{prdcts[1].name}</li>
#                 <li>{prdcts[2].name}</li>
#                 </ul>
#         """)

# def listeProduits(request):
#     prdct = Product.objects.all()
#     print(prdct)
#     return render(request, 'affichage_total.html', {'prdct': prdct})

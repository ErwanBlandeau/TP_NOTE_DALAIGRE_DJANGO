from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from app.forms import ContactUsForm, FournisseurForm, ProductAttributeForm, ProductForm, ProductFournisseurForm, ProductItemForm
from django.forms import BaseModelForm
from ..models import Fournisseur, Product, ProductAttribute, ProductFournisseur, ProductItem

class ProductUpdateView(UpdateView):
    model = Product
    form_class=ProductForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)


def ProductUpdate(request, id):
    prdct = Product.objects.get(id=id)
    print(prdct)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=prdct)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('product-detail', prdct.id)
    else:
        form = ProductForm(instance=prdct)
    return render(request,'product-update.html', {'form': form}) 


class ProductAttributeUpdateView(UpdateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('attribute-list')


def ProductAttributeUpdate(request, id):
    attr = ProductAttribute.objects.get(id=id)
    print(attr)
    if request.method == 'POST':
        form = ProductAttributeForm(request.POST, instance=attr)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('attribute-list')
    else:
        form = ProductAttributeForm(instance=attr)
    return render(request,'product-update.html', {'form': form}) 




class ProductItemUpdateView(UpdateView):
    model = ProductItem
    form_class = ProductItemForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('item-list')

    

def ProductItemUpdate(request, id):
    prdct = ProductItem.objects.get(id=id)
    if request.method == 'POST':
        form = ProductItemForm(request.POST, instance=prdct)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('product-detail', prdct.id)
    else:
        form = ProductItemForm(instance=prdct)
    return render(request,'product-update.html', {'form': form}) 



class FournisseurUpdateView(UpdateView):
    model = Fournisseur
    form_class = FournisseurForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('fournisseur-list')
    
    
def FournisseurUpdate(request, id):
    fournisseur = Fournisseur.objects.get(id=id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('fournisseur-list')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request,'product-update.html', {'form': form})



class ProductFournisseurUpdateView(UpdateView):
    model = Fournisseur
    form_class = FournisseurForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('fournisseur-list')
    
    
def ProductFournisseurUpdate(request, id):
    fournisseur = ProductFournisseur.objects.get(id=id)
    if request.method == 'POST':
        form = ProductFournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('fournisseur-list')
    else:
        form = ProductFournisseurForm(instance=fournisseur)
    return render(request,'product-update.html', {'form': form})
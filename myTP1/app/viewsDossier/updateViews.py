from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from app.forms import ContactUsForm, FournisseurForm, ProductAttributeForm, ProductForm, ProductFournisseurForm, ProductItemForm , StoreInventoryForm , CommandeForm
from django.forms import BaseModelForm
from ..models import Fournisseur, Product, ProductAttribute, ProductFournisseur, ProductItem, StoreInventory , Commande
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductUpdateView(UpdateView):
    model = Product
    form_class=ProductForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "modifier un produit" 
        return context


def ProductUpdate(request, id):
    prdct = Product.objects.get(id=id)
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

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "modifier un item produit" 
        return context

    

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "modifier un fournisseur" 
        return context
    
    
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
    model = ProductFournisseur
    form_class = ProductFournisseurForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdct = form.save()
        return redirect('each-fournisseur-product-list', prdct.fournisseur.id)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "modifier un produit du fournisseur" 
        return context
    
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




class StoreInventoryUpdateView(UpdateView):
    model = StoreInventory
    form_class = StoreInventoryForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdct = form.save()
        return redirect('each-market-inventory-list')    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Modifier un produit de l'inventaire" 
        return context
    
def StoreInventoryUpdate(request, id):
    fournisseur = StoreInventory.objects.get(id=id)
    if request.method == 'POST':
        form = StoreInventoryForm(request.POST, instance=fournisseur)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('each-market-inventory-list')
    else:
        form = StoreInventoryForm(instance=fournisseur)
    return render(request,'product-update.html', {'form': form})

@method_decorator(login_required, name="dispatch")
class CommandeUpdateView(UpdateView):
    model = Commande
    form_class = CommandeForm
    template_name = "update_total.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('commande-list')
    
    
def CommandeUpdate(request, id):
    commande = Commande.objects.get(id=id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=commande)
        if form.is_valid():
            # mettre à jour le produit existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du produit que nous venons de mettre à jour
            return redirect('commande-list')
    else:
        form = CommandeForm(instance=commande)
    return render(request,'product-update.html', {'form': form})
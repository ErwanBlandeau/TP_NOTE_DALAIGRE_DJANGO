from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from app.forms import ContactUsForm, ProductAttributeForm, ProductForm, ProductItemForm
from django.forms import BaseModelForm
from ..models import Product, ProductAttribute, ProductItem



# def home(request):
#     string = request.GET['name']
#     return HttpResponse("Bonjour %s!" % string)

# def home(request):
#     if request.GET and request.GET["test"]:
#         raise Http404
#     return render(request, 'base1.html', {'title': "Home",'var': "Bonjour Monde!"})

# def about(request):
#     return render(request, 'base1.html', {'title': "About",'var': "Abous us ...."})

# def contact(request):
#     return render(request, 'base1.html', {'title': "Contact",'var': "Contact us ...."})

# def accueil(request,param):
#     return render(request, 'base1.html', {'param': param, 'title': "Accueil",'var': "Accueil .... "})


class HomeView(TemplateView):
    template_name = "simplePage.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "simplePage.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    

class ContactView(TemplateView):
    template_name = "simplePage.html"
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Contact us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class HomeParamView(TemplateView):
    template_name = "simplePage.html"
    def get_context_data(self, **kwargs):
        context = super(HomeParamView, self).get_context_data(**kwargs
        )
        context['titreh1'] = "Hello " + self.kwargs['param']
        return context
    
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()
    return render(request, "contact.html",{'titreh1':titreh1, 'form':form})


def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "contact.html",{'titreh1':titreh1, 'form':form})


class EmailSentView(TemplateView):
    template_name = "email_sent.html"
    def get_context_data(self, **kwargs):
        context = super(EmailSentView, self).get_context_data(**kwargs)
        context['titreh1'] = "Email sent"
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name) 
    




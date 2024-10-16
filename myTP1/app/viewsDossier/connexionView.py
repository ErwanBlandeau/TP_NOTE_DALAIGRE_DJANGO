from django.shortcuts import render

# Create your views here.
from django.views.generic import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages




class ConnectView(LoginView):
    template_name = 'login.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'simplePage.html',{'titreh1':"hello "+username+", you're connected"})
        else:
            return render(request, 'register.html')
        

class RegisterView(TemplateView):
    template_name = 'register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', '').strip()  # Enlever les espaces superflus
        mail = request.POST.get('mail', '').strip()
        password = request.POST.get('password', '').strip()

        # Vérifiez que les champs ne sont pas vides
        if not username or not mail or not password:
            messages.error(request, "Tous les champs doivent être remplis.")
            return render(request, self.template_name)

        # Créer l'utilisateur
        try:
            user = User.objects.create_user(username=username, email=mail, password=password)
            user.save()
            messages.success(request, "Inscription réussie ! Vous pouvez vous connecter.")
            return render(request, 'login.html')
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, self.template_name)
        
class DisconnectView(TemplateView):
    template_name = 'logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
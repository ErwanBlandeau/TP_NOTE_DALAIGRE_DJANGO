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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import (
    ProductViewSet, FournisseurViewSet, ProductFournisseurViewSet, StoreInventoryViewSet,
    ProductItemViewSet, ProductAttributeViewSet, ProductAttributeValueViewSet, EtatViewSet,
    CommandeViewSet
)

# Configure the router
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'fournisseurs', FournisseurViewSet)
router.register(r'product-fournisseurs', ProductFournisseurViewSet)
router.register(r'store-inventories', StoreInventoryViewSet)
router.register(r'product-items', ProductItemViewSet)
router.register(r'product-attributes', ProductAttributeViewSet)
router.register(r'product-attribute-values', ProductAttributeValueViewSet)
router.register(r'etats', EtatViewSet)
router.register(r'commandes', CommandeViewSet)

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include(router.urls)),  # Include the router URLs
    path('monapp/', include('app.urls')),  # Include other app URLs
]

from django.db import models
from django.utils import timezone

PRODUCT_STATUS = (
    (0, 'Offline'),
    (1, 'Online'),
    (2, 'Out of stock')              
)

# Create your models here.
"""
    Status : numero, libelle
"""
class Status(models.Model):
    numero  = models.IntegerField()
    libelle = models.CharField(max_length=100)
          
    def __str__(self):
        return "{0} {1}".format(self.numero, self.libelle)
    
"""
Produit : nom, code, etc.
"""
class Product(models.Model):

    class Meta:
        verbose_name = "Produit"
        


    name          = models.CharField(max_length=100)
    code          = models.CharField(max_length=10, null=True, blank=True, unique=True)
    price_ht      = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True, verbose_name="Prix unitaire HT")
    price_ttc     = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True, verbose_name="Prix unitaire TTC")
    status        = models.SmallIntegerField(choices=PRODUCT_STATUS, default=0)
    date_creation = models.DateTimeField(blank=True, verbose_name="Date création") 
    nombre_de_produit = models.IntegerField(null=True, blank=True, verbose_name="Nombre de produits")
    #fields = '__all__'
    exclude = ('price_ttc', 'status')
    
    def __str__(self):
        return "{0} {1}".format(self.name, self.code)
    
    

"""
Fournisseur : nom, code, etc.
"""
class Fournisseur(models.Model):

    class Meta:
        verbose_name = "Fournisseur"

    name            = models.CharField(max_length=100, verbose_name="Nom du fournisseur")
    code            = models.CharField(max_length=10, unique=True, verbose_name="Code du fournisseur")
    email           = models.EmailField(max_length=100, verbose_name="Adresse email")
    phone           = models.CharField(max_length=20, verbose_name="Numéro de téléphone", null=True, blank=True)
    address         = models.TextField(null=True, blank=True, verbose_name="Adresse")
    website         = models.URLField(max_length=200, null=True, blank=True, verbose_name="Site web")

    def __str__(self):
        return f"{self.name} - {self.code}"
    

"""
    Déclinaison de produit déterminée par des attributs comme la couleur, etc.
"""
class ProductItem(models.Model):
    
    class Meta:
        verbose_name = "Déclinaison Produit"

    color   = models.CharField(max_length=100)
    code    = models.CharField(max_length=10, null=True, blank=True, unique=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attributes  = models.ManyToManyField("ProductAttributeValue", related_name="product_item", null=True, blank=True)
       
    def __str__(self):
        return "{0} {1}".format(self.color, self.code)
    
class ProductAttribute(models.Model):
    """
    Attributs produit
    """
    
    class Meta:
        verbose_name = "Attribut"
        
    name =  models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ProductAttributeValue(models.Model):
    """
    Valeurs des attributs
    """
    
    class Meta:
        verbose_name = "Valeur attribut"
        ordering = ['position']
        
    value              = models.CharField(max_length=100)
    product_attribute  = models.ForeignKey('ProductAttribute', verbose_name="Unité", on_delete=models.CASCADE)
    position           = models.PositiveSmallIntegerField("Position", null=True, blank=True)
     
    def __str__(self):
        return "{0} [{1}]".format(self.value, self.product_attribute)
    
class Etat(models.Model):
    nomEtat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomEtat
 
"""
Fournisseur : fournisseur, produit, quantite_du_produit , etat , date_creation.
"""
    
class Commande(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite_du_produit = models.IntegerField(null=True, blank=True)
    etat = models.ForeignKey(Etat, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date création")

    class Meta:
        verbose_name = "Commande"
        unique_together = ('fournisseur', 'produit')  # Assure qu'une commande pour le même fournisseur et produit est unique

    def __str__(self):
        return f"Commande de {self.produit} par {self.fournisseur} le {self.date_creation}"
    

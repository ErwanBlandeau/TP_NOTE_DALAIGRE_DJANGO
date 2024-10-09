
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
    






# ----------------- TP NOTEE -----------------

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
Produit : nom, code, etc.
"""
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du produit")
    code = models.CharField(max_length=10, null=True, blank=True, unique=True, verbose_name="Code du produit")
    price_ht = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix unitaire HT")
    price_ttc = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix unitaire TTC")
    status = models.SmallIntegerField(choices=PRODUCT_STATUS, default=0, verbose_name="Statut")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    nombre_de_produit = models.IntegerField(null=True, blank=True, verbose_name="Nombre de produits")
    # Relation avec Fournisseur via un modèle intermédiaire ProductFournisseur
    fournisseurs = models.ManyToManyField("Fournisseur", related_name="products", through="ProductFournisseur", verbose_name="Fournisseurs")
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class ProductFournisseur(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit")
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, verbose_name="Fournisseur")
    prix_fournisseur = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix fournisseur")
    
    class Meta:
        verbose_name = "Fournisseur Produit"
        unique_together = ('product', 'fournisseur')

    def __str__(self):
        return f"{self.fournisseur.name} fournit {self.product.name} (Prix: {self.prix_fournisseur})"

class StoreInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit")
    quantity_in_stock = models.IntegerField(default=0, verbose_name="Quantité en stock")
    price_in_store = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix en magasin")

    class Meta:
        verbose_name = "Inventaire Magasin"
        unique_together = ('product', )

    def __str__(self):
        return f"{self.product.name} - {self.quantity_in_stock} en stock (Prix: {self.price_in_store})"
    
 
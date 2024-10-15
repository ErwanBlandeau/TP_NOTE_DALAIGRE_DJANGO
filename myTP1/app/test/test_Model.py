import unittest
from django.test import TestCase
from django.db import IntegrityError
from app.models import Product, ProductAttribute, ProductAttributeValue

class ProductTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="T-Shirt", 
            code="TS001",
            price_ht=19.99,
            price_ttc=23.99,
            status=1,
            date_creation="2023-10-01",
            nombre_de_produit=100
        )

    def test_create_product(self):
        self.assertEqual(self.product.name, "T-Shirt")
        self.assertEqual(self.product.code, "TS001")
        self.assertEqual(self.product.price_ht, 19.99)
        self.assertEqual(self.product.price_ttc, 23.99)
        self.assertEqual(self.product.status, 1)
        self.assertEqual(self.product.date_creation, "2023-10-01")
        self.assertEqual(self.product.nombre_de_produit, 100)

    def test_product_str(self):
        self.assertEqual(str(self.product), "T-Shirt TS001")

    def test_product_update(self):
        self.product.name = "Sweater"
        self.product.save()
        self.assertEqual(self.product.name, "Sweater")

    def test_product_delete(self):
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)

    def test_product_without_name(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(code="NP001", price_ht=9.99, price_ttc=11.99)

    def test_product_duplicate(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(name="T-Shirt", code="TS001", price_ht=19.99, price_ttc=23.99)

    def test_product_price_update(self):
        self.product.price_ht = 24.99
        self.product.price_ttc = 29.99
        self.product.save()
        self.assertEqual(self.product.price_ht, 24.99)
        self.assertEqual(self.product.price_ttc, 29.99)

    def test_product_description_update(self):
        self.product.description = "A stylish t-shirt"
        self.product.save()
        self.assertEqual(self.product.description, "A stylish t-shirt")







import unittest
from django.test import TestCase
from django.db import IntegrityError
from app.models import ProductAttributeValue, ProductAttribute
from app.models import Fournisseur
from app.models import ProductFournisseur

class ProductAttributeValueTestCase(TestCase):

    def setUp(self):
        self.product_attribute = ProductAttribute.objects.create(name="Color")

    def test_create_product_attribute_value(self):
        pav = ProductAttributeValue.objects.create(
            value="Red",
            product_attribute=self.product_attribute,
            position=1
        )
        self.assertEqual(pav.value, "Red")
        self.assertEqual(pav.product_attribute, self.product_attribute)
        self.assertEqual(pav.position, 1)

    def test_product_attribute_value_str(self):
        pav = ProductAttributeValue.objects.create(
            value="Large",
            product_attribute=self.product_attribute,
            position=2
        )
        self.assertEqual(str(pav), "Large [Color]")

    def test_product_attribute_value_ordering(self):
        pav1 = ProductAttributeValue.objects.create(
            value="Cotton",
            product_attribute=self.product_attribute,
            position=2
        )
        pav2 = ProductAttributeValue.objects.create(
            value="Polyester",
            product_attribute=self.product_attribute,
            position=1
        )
        pavs = ProductAttributeValue.objects.all()
        self.assertEqual(pavs[0], pav2)
        self.assertEqual(pavs[1], pav1)

    def test_product_attribute_value_position_null(self):
        pav = ProductAttributeValue.objects.create(
            value="Light",
            product_attribute=self.product_attribute,
            position=None
        )
        self.assertIsNone(pav.position)

    def test_product_attribute_value_blank_position(self):
        pav = ProductAttributeValue.objects.create(
            value="Medium",
            product_attribute=self.product_attribute,
            position=None
        )
        self.assertIsNone(pav.position)

    def test_product_attribute_value_without_position(self):
        pav = ProductAttributeValue.objects.create(
            value="Blue",
            product_attribute=self.product_attribute
        )
        self.assertIsNone(pav.position)

    def test_product_attribute_value_without_product_attribute(self):
        with self.assertRaises(IntegrityError):
            ProductAttributeValue.objects.create(
                value="Green",
                position=1
            )
            
class FournisseurTestCase(TestCase):

    def setUp(self):
        self.fournisseur = Fournisseur.objects.create(
            name="Supplier A",
            code="SUP001",
            email="supplierA@example.com",
            phone="1234567890",
            address="123 Supplier Street",
            website="http://www.supplierA.com"
        )

    def test_create_fournisseur(self):
        self.assertEqual(self.fournisseur.name, "Supplier A")
        self.assertEqual(self.fournisseur.code, "SUP001")
        self.assertEqual(self.fournisseur.email, "supplierA@example.com")
        self.assertEqual(self.fournisseur.phone, "1234567890")
        self.assertEqual(self.fournisseur.address, "123 Supplier Street")
        self.assertEqual(self.fournisseur.website, "http://www.supplierA.com")

    def test_fournisseur_str(self):
        self.assertEqual(str(self.fournisseur), "Supplier A - SUP001")

    def test_fournisseur_update(self):
        self.fournisseur.name = "Supplier B"
        self.fournisseur.save()
        self.assertEqual(self.fournisseur.name, "Supplier B")

    def test_fournisseur_delete(self):
        fournisseur_id = self.fournisseur.id
        self.fournisseur.delete()
        with self.assertRaises(Fournisseur.DoesNotExist):
            Fournisseur.objects.get(id=fournisseur_id)

    def test_fournisseur_duplicate_code(self):
        with self.assertRaises(IntegrityError):
            Fournisseur.objects.create(name="Supplier C", code="SUP001", email="supplierC@example.com")

    def test_fournisseur_email_update(self):
        self.fournisseur.email = "newemail@example.com"
        self.fournisseur.save()
        self.assertEqual(self.fournisseur.email, "newemail@example.com")

    def test_fournisseur_blank_phone(self):
        self.fournisseur.phone = ""
        self.fournisseur.save()
        self.assertEqual(self.fournisseur.phone, "")

    def test_fournisseur_blank_address(self):
        self.fournisseur.address = ""
        self.fournisseur.save()
        self.assertEqual(self.fournisseur.address, "")

    def test_fournisseur_blank_website(self):
        self.fournisseur.website = ""
        self.fournisseur.save()
        self.assertEqual(self.fournisseur.website, "")


class ProductFournisseurTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="T-Shirt", 
            code="TS001",
            price_ht=19.99,
            price_ttc=23.99,
            status=1,
            date_creation="2023-10-01",
            nombre_de_produit=100
        )
        self.fournisseur = Fournisseur.objects.create(
            name="Supplier A",
            code="SUP001",
            email="supplierA@example.com",
            phone="1234567890",
            address="123 Supplier Street",
            website="http://www.supplierA.com"
        )
        self.product_fournisseur = ProductFournisseur.objects.create(
            product=self.product,
            fournisseur=self.fournisseur,
            prix_fournisseur=15.99
        )

    def test_create_product_fournisseur(self):
        self.assertEqual(self.product_fournisseur.product, self.product)
        self.assertEqual(self.product_fournisseur.fournisseur, self.fournisseur)
        self.assertEqual(self.product_fournisseur.prix_fournisseur, 15.99)

    def test_product_fournisseur_str(self):
        self.assertEqual(str(self.product_fournisseur), "Supplier A fournit T-Shirt (Prix: 15.99)")

    def test_product_fournisseur_update(self):
        self.product_fournisseur.prix_fournisseur = 17.99
        self.product_fournisseur.save()
        self.assertEqual(self.product_fournisseur.prix_fournisseur, 17.99)

    def test_product_fournisseur_delete(self):
        product_fournisseur_id = self.product_fournisseur.id
        self.product_fournisseur.delete()
        with self.assertRaises(ProductFournisseur.DoesNotExist):
            ProductFournisseur.objects.get(id=product_fournisseur_id)


    def test_product_fournisseur_duplicate(self):
        with self.assertRaises(IntegrityError):
            ProductFournisseur.objects.create(
                product=self.product,
                fournisseur=self.fournisseur,
                prix_fournisseur=15.99
            )


from decimal import Decimal 
from django.test import TestCase
import unittest

from .models import Supplier, Product

# Create your tests here.
class SupplierModelTestCase(TestCase):
    def setUp(self):
        # Luo testitietokantaan esimerkkitoimittaja ennen jokaista testiä
        self.supplier = Supplier.objects.create(
            companyname="Test Company",
            contactname="John Doe",
            address="123 Test St",
            phone="+1234567890",
            email="john@test.com",
            country="Testland"
        )
    def test_supplier_creation(self):
        # testaa että toimittaja luotiin oikein
        supplier = Supplier.objects.get(companyname="Test Company")
        self.assertEqual(supplier.contactname, "John Doe")
        self.assertEqual(supplier.address, "123 Test St")
        self.assertEqual(supplier.phone, "+1234567890")
        self.assertEqual(supplier.email, "john@test.com")
        self.assertEqual(supplier.country, "Testland")


class ProductModelTestCase(TestCase):
    def setUp(self):
        # Luo testitietokantaan esimerkkitoimittaja ja tuote ennen jokaista testiä
        # 1. Сначала СОЗДАЕМ поставщика (Supplier) в тестовой БД
        self.supplier = Supplier.objects.create(
            companyname="Test Company",
            contactname="John Doe",
            address="123 Test St",
            phone="+1234567890",
            email="john@test.com",
            country="Testland"
        )
        # 2. Теперь создаем продукт, ссылаясь на созданного поставщика
        self.product = Product.objects.create(
            productname="Test Product",
            packagesize="10 boxes",
            unitprice=19.99,
            unitsinstock=100,
            supplier=self.supplier
        )
    def test_product_creation(self):
        """Test that a product was created correctly and its fields are saved."""
        # testaa että tuote luotiin oikein
        product = Product.objects.get(productname="Test Product")
        self.assertEqual(product.packagesize, "10 boxes")
        self.assertEqual(product.unitprice, Decimal('19.99'))
        self.assertEqual(product.unitsinstock, 100)
        # ДОПОЛНИТЕЛЬНО И ОЧЕНЬ ВАЖНО: проверяем связь с поставщиком
        self.assertEqual(product.supplier, self.supplier)
        self.assertEqual(product.supplier.companyname, "Test Company")

    # Дополнительный тест для проверки метода __str__
    def test_product_string_representation(self):
        """Test the __str__ method of the Product model."""
        expected_str = f"{self.product.productname} produced by {self.supplier.companyname}"
        self.assertEqual(str(self.product), expected_str)

    @unittest.expectedFailure
    def test_product_creation_failure(self):
        # tämä testi on tarkoitettu epäonnistumaan
        self.assertEqual(self.product.unitprice, 20.00)
# TDD - Test Driven Development

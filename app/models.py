from django.db import models

# Create your models here.
class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="New firma")
    contactname = models.CharField(max_length = 50, default="John Doe")
    address = models.CharField(max_length = 100, default="Newstreet 1")
    phone = models.CharField(max_length = 20, default="+358401234567")
    email = models.CharField(max_length = 50, default="john.doe@newfirma.com")
    country = models.CharField(max_length = 50, default="England")
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.companyname} from {self.country}"


class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa hienommin,
     # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"
    
class Customer(models.Model):
    companyname = models.CharField(max_length=100)
    contactname = models.CharField(max_length=100)
    contactemail = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.companyname

class Order(models.Model):
    ORDER_STATUS = [
        ('PND', 'Pending'),
        ('CMP', 'Completed'),
        ('CNC', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Связь с существующей моделью!
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=ORDER_STATUS, default='PND')

    def __str__(self):
        return f"Order #{self.id} by {self.customer.companyname}"

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    serial_number = models.CharField(max_length=100, unique=True, null=True) 
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True) 

    def __str__(self):
        return f'{self.name} - {self.serial_number}'

class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    order_date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('received', 'Received'),  
        ('returned', 'Returned'),  
        ('denied', 'Denied'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    @property
    def total_price(self):
        return self.order_quantity * self.name.unit_price  

    def __str__(self):
        return f'{self.employee} - {self.name} - {self.status}'

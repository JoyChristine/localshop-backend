from django.db import models
from django.contrib.auth.models import User


STATUS = (
    ('1','Paid'),
    ('2','Unpaid'),
    
)
# superuser ===> invite to the admin(manager)  ==>login -- add clerk
# Create your models here.
# admin, clerk , products, store , reports,orders, defectivegoods

class Admin(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    
    # password = models.CharField(max_length=20)

class Clerk(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

class Product(models.Model):
    CATEGORY = (
    ('1','electronics'),('2','foods'),('3','detergents'),('4','kitchen-ware'),('5','toys')
)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity = models.ForeignKey('Order',on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS,null=True)
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()
    expiry_date = models.DateTimeField()
    # defective = models.ForeignKey('defectivegood', on_delete=models.DO_NOTHING,null=True)
    # Ask whether it should be interger or not

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    ordered_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Store(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
    clerk = models.ForeignKey(Clerk, on_delete=models.DO_NOTHING)

class defectivegood(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    clerk = models.ForeignKey(Clerk, on_delete=models.DO_NOTHING)
    



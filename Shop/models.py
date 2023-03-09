from django.db import models
from Account.models import Account

# Create your models here.

class Shop_categories(models.Model):
    Name_of_categories=models.CharField(max_length=25,unique=True)
    Copune_code=models.CharField(max_length=50,default="",blank=True)
    class Meta:
        db_table='Shop_categories'
    

class Shop(models.Model):
    add_by=models.ForeignKey(Account,on_delete=models.DO_NOTHING)
    image=models.ImageField(upload_to="Shop_products")
    Product_name=models.CharField(max_length=25,unique=True)
    Discount_price=models.FloatField()
    Actual_price=models.FloatField()
    Rate=models.PositiveIntegerField(default=0,blank=True)
    product_details=models.JSONField()
    quantity=models.PositiveBigIntegerField(default='0',blank=True)
    category=models.ForeignKey(Shop_categories,on_delete=models.DO_NOTHING)
    class Meta:
        db_table='Shop'

class comment(models.Model):
    product=models.ForeignKey(Shop,on_delete=models.DO_NOTHING)
    addby=models.ForeignKey(Account,on_delete=models.DO_NOTHING)
    comments=models.JSONField()
    class Meta:
        db_table='comment'
from django.db import models
from Account.models import Account
from django.core.validators import MaxValueValidator
from django_fields import DefaultStaticImageField

# Create your models here.

class Card(models.Model):
    add_by=models.ForeignKey(Account,on_delete=models.DO_NOTHING)
    Image=DefaultStaticImageField(upload_to="Grading_card_Img",default_image_path='images/blank.png',blank=True)
    NFC_No=models.PositiveBigIntegerField(validators=[MaxValueValidator(99999)],unique=True)
    Card_Name=models.CharField(max_length=25)
    Card_No=models.CharField(max_length=10)
    Rarity=models.CharField(max_length=25)
    Year=models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    Series=models.CharField(max_length=25)
    Game=models.CharField(max_length=25)
    Overall_Grade=models.CharField(max_length=10)
    Centering=models.FloatField()
    Surface=models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    Edges=models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    Corners=models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    Notes=models.CharField(max_length=20)
    shop=models.BooleanField()
    class Meta:
        db_table='Card'


class Submited_Cards(models.Model):
    user=models.OneToOneField(Account,on_delete=models.DO_NOTHING)
    image=models.ImageField(upload_to='Submitted_cards')
    Card_name=models.CharField(max_length=50) 
    Year=models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    Card_No=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    Rarity=models.CharField(max_length=25)
    Declared_Amt=models.PositiveBigIntegerField()
    Service_type=models.CharField(max_length=30)
    Recived=models.BooleanField(default=False)
    class Meta:
        db_table='Submited_Cards'



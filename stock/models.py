from django.db import models
from django.db.models.deletion import SET_DEFAULT
from typing import OrderedDict

# Create your models here.

FEETs = (('6', '6'),
		('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
		) 

TYPEs = (('মোটা ঢেউ', 'মোটা ঢেউ'),
		('চিকন ঢেউ', 'চিকন ঢেউ'),
        ('NOF', 'NOF'),
        ('লোম','লোম'),
        ('কালার','কালার'),
        ('বক্স-কালার','বক্স-কালার'),
		) 

MMs = (('120', '120'),
		('150', '150'),
        ('170', '170'),
        ('190', '190'),
        ('200', '200'),
        ('260', '260'),
        ('320', '320'),
        ('340', '340'),
        ('420', '420'),
        ('25', '25'),
        ('30', '30'),
        ('48', '48'),
		) 


class Product(models.Model):
    pieces = models.IntegerField(default=0)
    feet = models.CharField(max_length=200,null=True,choices=FEETs)
    mm = models.CharField(max_length=200,null=True,choices=MMs)
    types = models.CharField(max_length=200,null=True,choices= TYPEs)
    

    class Meta:
        ordering = ['mm','feet'] #Sort in desc order

    def __str__(self):
		    return f"{self.mm} ----> {self.feet} ----- {self.types}"

class History(models.Model):
    name = models.CharField(max_length=200,null=True)
    date = models.DateField()
    pieces = models.IntegerField(default=0)
    feet = models.CharField(max_length=200,null=True,choices=FEETs)
    mm = models.CharField(max_length=200,null=True,choices=MMs)
    types = models.CharField(max_length=200,null=True,choices= TYPEs)
    


    def __str__(self):
        return f"{self.date} -> {self.feet} × {self.mm} -----{self.types}"



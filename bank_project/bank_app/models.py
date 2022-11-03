import uuid

from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.
from django.shortcuts import redirect

Choices=[
    ('Thiruvanathapuram','tvm'),
    ('Ernakulam','ekm'),
    ('Calicut','clt'),
    ('Thrissur','thr'),
    ('Kottayam','ktym')

]
class Branches(models.Model):
    name=models.CharField(max_length=100,unique=True,choices=Choices)
    slug=models.SlugField(max_length=100,unique=True)
    link=models.CharField(max_length=500,blank=True)
    class Meta:
        ordering=['name',]
        verbose_name='district'
        verbose_name_plural='districts'


    def __str__(self):
        return self.name
gender_choice=(
    ('Male','Male'),
    ('Female','Female'),
    ('Transgender','Transgender')
)

class City(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=199,unique=True)
    branch=models.ForeignKey(Branches,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

account_choices=[
    ('Savings Account','Savings Account'),
    ('Current Account','Current Account')
]

mat_choices=[
    ("Credit Card",'Credit Card'),
    ('Debit Card','Debit Card'),
    ('Pass Book','Pass Book')
]



class Task(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,default=uuid.uuid1)
    dob=models.DateField(blank=True)
    age=models.IntegerField(blank=True)
    gender=models.CharField(max_length=30,choices=gender_choice)
    phonenumber=models.IntegerField(blank=True)
    mailid=models.EmailField(max_length=300,blank=True)
    address=models.TextField(max_length=200,blank=True)
    district=models.ForeignKey(Branches,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    account=models.CharField(max_length=200,choices=account_choices)
    material=MultiSelectField(choices=mat_choices)

    class Meta:
        ordering=['name',]
        verbose_name='task'
        verbose_name_plural='tasks'

    def __str(self):
        return  self.name


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=30)
    class Meta:
        db_table = "student"
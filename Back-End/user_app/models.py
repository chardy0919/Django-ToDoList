# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core import validators as v

# # Create your models here.
# class Person(AbstractUser):
#     email= models.EmailField(
#         verbose_name ='email address',
#         unique=True,
#     )
#     age=models.IntegerField(validators=[v.MinValueValidator(0),v.MaxValueValidator(150)])
#     display_name=models.CharField(null=True, blank=True, unique=True)
#     address= models.CharField(null=True, blank=True)
#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS=[]
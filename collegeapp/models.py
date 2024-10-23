from django.db import models
from login.models import UserProfile

# Create your models here.
class Collegeprofile(models.Model):
    login_id=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    college_id=models.CharField(max_length=20,null=True,blank=True)
    collegename=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone_no=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    
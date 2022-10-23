from django.db import models

# Create your models here.

class ContactU(models.Model):
    email=models.EmailField(max_length=150)
    mobile_1=models.IntegerField()
    mobile_2=models.IntegerField()
    
        
class StudentApplication(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    app_type=models.CharField(max_length=20)  
    tenure=models.CharField(max_length=20)
    reg_id=models.CharField(max_length=10)
    email_id=models.EmailField(max_length=30)
    aadhar_no=models.CharField(max_length=20)
    address=models.TextField(max_length=200)
    station=models.CharField(max_length=20)
    junction=models.CharField(max_length=20,blank=True)      
    date=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10,null=True,unique=True)
    
    def __str__(self):
        return f" {self.first_name} {self.last_name}"
    
class FileUpload(models.Model):
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    reg_id=models.CharField(max_length=20)
    file=models.FileField(null=True) 
    feedbacks=models.TextField(max_length=200 ,null=True,blank=True)
    def __str__(self):
        return f" {self.f_name} {self.l_name}"
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime,timedelta



class Book(models.Model):
    book_id=models.AutoField
    book_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    category = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='myapp/images',default="")
    image1 = models.ImageField(upload_to='myapp/images',default="")
    issued_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    issued_date = models.DateField(blank=True, null=True)
    
    
    
    def __str__(self):
           return self.book_name
       

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20,default="")
    Faculty= models.CharField(max_length=20,default="")
    Batch=models.CharField(max_length=20,default="")
    image2 = models.ImageField(upload_to='myapp/images',default="")
    # Add other fields specific to the student profile

    def __str__(self):
        return self.user.username

class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book} - {self.student.username}"
#0
from django.db import models

# Create your models here.
class Users(models.Model):
    status = [
        ('member','Member'),
        ('admin','Admin')
    ]

    firstname = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=60,null=False)
    role = models.CharField(max_length=20, choices=status, default='member')

class Posts(models.Model):
    post_title = models.CharField(max_length=50,null=False)
    post_thumbnail = models.ImageField(max_length=200,null=True)
    post_sfdc = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=False,related_name='posts')
    ulike_post = models.ManyToManyField(Users,related_name='liked_posts',null=True)

class Products(models.Model):
    description = models.CharField(max_length=256,null=False)
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    post_date = models.DateField(auto_now_add=True)
    img_src = models.ImageField(null=True, blank=True, upload_to = 'images/')
    post = models.OneToOneField(Posts,on_delete=models.CASCADE,related_name='products',default='')

class Feedbacks(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=256,null=False)

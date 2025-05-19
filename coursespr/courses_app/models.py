from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    ROLE_CHOICES=(
        ('students','students'),
        ('teachers','teachers')
    )
    role = models.CharField(choices=ROLE_CHOICES,max_length=15)
    user_image = models.ImageField(upload_to='user_images/',null=True,blank=True)
    bio_teach= models.TextField(max_length=50)
class Category(models.Model):
    category_name = models.CharField(max_length=30)
class Networks(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    network_name = models.CharField(max_length=30,unique=True)
    network_link = models.URLField()
class Courses(models.Model):
    course_name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    LEVEL_CHOICES = (
        ('beginner','beginner'),
        ('elementary','elementary'),
        ('advanced','advanced')
    )

    level = models.CharField(choices=LEVEL_CHOICES,max_length=16)
    price = models.PositiveSmallIntegerField(null=True,blank=True)
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)








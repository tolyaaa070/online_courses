from random import choices

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

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField(null=True, blank=True)
    content = models.TextField()
    course = models.URLField(null=True, blank=True)

class Assignment(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    due_date = models.DateField()
    course = models.URLField(null=True, blank=True)
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class ExamQuestion(models.Model):
    question_name = models.CharField(max_length=139)
    score = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    exam = models.ForeignKey(Assignment, on_delete=models.CASCADE)

class Options(models.Model):
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=145)
    check_var = models.BooleanField()

class Certificate(models.Model):
    student = models.ForeignKey(UserProfile,related_name='students', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,related_name='sert_courses', on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.URLField(null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile,related_name='users', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, related_name='courses',  on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i))for  i in range(1, 6)])
    comment = models.TextField()











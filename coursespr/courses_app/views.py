from .models import *
from .serializers import (ReviewSerializer, CertificateSerializer, OptionsSerializer, ExamQuestionSerializer,
                          AssignmentSerializer, LessonSerializer, CoursesSerializer, CategorySerializer,
                          NetworksSerializer, UserProfileSerializer, )
from rest_framework import viewsets, generics

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Networks.objects.all()
    serializer_class = NetworksSerializer

class CoursesAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ExamQuestionViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer

class OptionsViewSet(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




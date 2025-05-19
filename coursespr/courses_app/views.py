from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import (ReviewSerializer, CertificateSerializer, OptionsSerializer, ExamQuestionSerializer,
                          AssignmentListSerializer,AssignmentDetailSerializer, LessonSerializer,
                          CoursesListSerializer,CoursesDetailSerializer, CategorySerializer,
                          NetworksSerializer, UserProfileSerializer, )
from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permission import CheckRole, CheckRoleReview


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
    serializer_class = CoursesListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['level']
    search_fields = ['course_name']
    ordering_fields = ['price']



class CoursesDetailAPIView(generics.RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesDetailSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class AssignmentAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']


class AssignmentDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer
    permission_classes = [CheckRole]

class ExamQuestionViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer

class OptionsViewSet(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ReviewAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckRoleReview]




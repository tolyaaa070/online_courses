from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import (ReviewSerializer, CertificateSerializer, OptionsSerializer, ExamQuestionSerializer,
                          AssignmentListSerializer,AssignmentDetailSerializer, LessonSerializer,
                          CoursesListSerializer,CoursesDetailSerializer,
                          CategorySerializer,LoginSerializer,UserSerializer,
                          NetworksSerializer, UserProfileSerializer, )
from rest_framework import viewsets, generics, permissions,status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permission import CheckRole, CheckRoleReview
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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




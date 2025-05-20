from .views import (UserProfileViewSet, CategoryViewSet, NetworkViewSet, CoursesAPIView,
                    LessonViewSet, AssignmentAPIView,AssignmentDetailAPIView,LogoutView,
                    ExamQuestionViewSet, OptionsViewSet,CoursesDetailAPIView,CustomLoginView,
                    ReviewAPIView, RegisterView)
from rest_framework import routers
from django.urls import path



router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'category', UserProfileViewSet, basename='categories')


urlpatterns = [


    path('exam/', AssignmentAPIView.as_view(), name='exams'),
    path('exam/<int:pk>/', AssignmentDetailAPIView.as_view(), name='exam-detail'),

    path('courses/', CoursesAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>', CoursesDetailAPIView.as_view(), name='courses_detail'),

    path('review/', ReviewAPIView.as_view(), name='reviews'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]



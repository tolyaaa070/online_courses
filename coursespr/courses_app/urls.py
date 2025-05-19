from .views import (UserProfileViewSet, CategoryViewSet, NetworkViewSet, CoursesAPIView,
                    LessonViewSet, AssignmentViewSet, ExamQuestionViewSet, OptionsViewSet,
                    ReviewViewSet)
from rest_framework import routers
from django.urls import path



router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'review', ReviewViewSet, basename='reviews')
router.register(r'category', UserProfileViewSet, basename='categories')

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
]



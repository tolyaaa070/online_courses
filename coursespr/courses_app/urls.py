from .views import (UserProfileViewSet, CategoryViewSet, NetworkViewSet, CoursesAPIView,
                    LessonViewSet, AssignmentAPIView,AssignmentDetailAPIView,
                    ExamQuestionViewSet, OptionsViewSet,CoursesDetailAPIView,
                    ReviewViewSet)
from rest_framework import routers
from django.urls import path



router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'review', ReviewViewSet, basename='reviews')
router.register(r'category', UserProfileViewSet, basename='categories')

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('exam/', AssignmentAPIView.as_view(), name='exams'),
    path('exam/<int:pk>/', AssignmentDetailAPIView.as_view(), name='exam-detail'),
    path('courses/', CoursesAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>', CoursesDetailAPIView.as_view(), name='courses_detail')
]



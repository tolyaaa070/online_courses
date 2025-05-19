from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NetworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networks
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_image','course_name', 'price', 'created_by',]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CoursesDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    created_by = UserProfileSerializer()
    # category = CategorySerializer()
    # category = serializers.SlugRelatedField(read_only=True, slug_field='category_name')
    class Meta:
        model = Courses
        fields = ['id', 'course_image','course_name', 'price', 'created_by',
                  'description','created_at', 'level', 'category', 'lessons', 'reviews']


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['option_name', 'check_var']

class ExamQuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(read_only=True, many=True)

    class Meta:
        model = ExamQuestion
        fields = ['question_name', 'score', 'options']

class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    exam_questions = ExamQuestionSerializer(read_only=True, many=True)
    class Meta:
        model = Assignment
        fields = [ 'title', 'exam_questions', ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'



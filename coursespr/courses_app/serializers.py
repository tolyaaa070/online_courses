from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                   'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

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
        fields = ['id', 'title', 'content', 'video']

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
    created_at = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    # category = CategorySerializer()
    category = serializers.SlugRelatedField(many=True,read_only=True, slug_field='category_name')
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



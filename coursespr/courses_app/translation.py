from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('bio_teach',)

@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Networks)
class ProductTranslationOptions(TranslationOptions):
    fields = ('network_name',)

@register(Courses)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Lesson)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Assignment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','description',)

@register(ExamQuestion)
class ProductTranslationOptions(TranslationOptions):
    fields = ('question_name',)

@register(Options)
class ProductTranslationOptions(TranslationOptions):
    fields = ('option_name',)

@register(Review)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)





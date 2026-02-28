from django.contrib import admin
from django.contrib.auth.models import User

from .models import Course, Lesson, Enrollment, Question, Choice, Submission


# Inline for Choice inside Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Inline for Question inside Course
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')


# Register models
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Submission)
admin.site.register(Question, QuestionAdmin)
admin.site.register(User)

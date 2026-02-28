from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:course_id>/', views.submit_exam, name='submit_exam'),
    path('result/<int:submission_id>/', views.show_exam_result, name='exam_result'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Path to submit the exam
    path('submit/<int:course_id>/', views.submit_exam, name='submit_exam'),
    
    # Path to display and evaluate the exam result
    path('result/<int:submission_id>/', views.show_exam_result, name='exam_result'),
]

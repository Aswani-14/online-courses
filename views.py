from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Submission, Choice

def submit_exam(request, course_id):
    """
    Handles exam submission:
    - Gets selected choices from POST request
    - Creates a Submission object
    - Redirects to the exam result page
    """
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')
        enrollment = Enrollment.objects.get(user=request.user, course_id=course_id)

        submission = Submission.objects.create(enrollment=enrollment)
        submission.choices.set(selected_choices)

        return redirect('exam_result', submission.id)

def show_exam_result(request, submission_id):
    """
    Evaluates the submitted exam and renders the result template.
    """
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.enrollment.course

    total_score = 0
    obtained_score = 0

    for question in course.question_set.all():
        total_score += question.grade
        correct_choices = set(question.choice_set.filter(is_correct=True))
        selected_choices = set(submission.choices.filter(question=question))

        if correct_choices == selected_choices:
            obtained_score += question.grade

    context = {
        'submission': submission,
        'course': course,
        'score': obtained_score,
        'total': total_score
    }

    return render(request, 'exam_result.html', context)

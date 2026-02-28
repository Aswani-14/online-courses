from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment, Submission, Choice

@login_required
def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

    if request.method == 'POST':
        selected_choice_ids = request.POST.getlist('choice')
        submission = Submission.objects.create(enrollment=enrollment)
        submission.choices.set(selected_choice_ids)
        return redirect('exam_result', submission_id=submission.id)

    return redirect('course_detail', course_id=course.id)

@login_required
def show_exam_result(request, submission_id):
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

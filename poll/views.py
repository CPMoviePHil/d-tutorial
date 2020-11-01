from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse
from .models import Questions, Answers
# Create your views here.


def index(request):
    latest_question_list = Questions.objects.order_by('-publication_date')[:5]
    fuckyou = "fuckyou"
    return render(request, 'poll/index.html', {'latest_question_list': latest_question_list, "fuckyou":fuckyou})


def detail(request, question_id):
    try:
        question = Questions.objects.get(q_text=question_id)
    except Questions.DoesNotExist:
        raise Http404('question is not found')
    return render(request, "poll/detail.html", {"q": question})

def detail2(request, qid):
    try:
        question = get_object_or_404(Questions, pk=qid)
    except Questions.DoesNotExist:
        raise Http404("Question not found!")
    return render(request, 'poll/detail.html', {"q": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def forNotFound():
    pass

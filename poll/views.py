from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions, Answers
# Create your views here.



def index(request):
    latest_question_list = Questions.objects.order_by('-publication_date')[:5]
    return render(request, 'poll/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     import json
#     from urllib import request
#     url = 'https://www.xtube.com/webmaster/api/getcategorylist/'
#     data = request.urlopen(url).read().decode("utf-8")
#     return render(request, 'poll/forapi.html', {'data': data})
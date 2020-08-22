from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from .models import  Question

from django.http import  Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
    response = "you're looking at the result fo question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
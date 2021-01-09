from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.


def index(req):
    # return HttpResponse("Hello cac ban!!!")
    my_name = 'Lam Huynh'
    info = ["25 years old", "backend developer", "Love technologies"]
    return render(req, "polls/index.html", {"name": my_name, "personal": info})


def showQuestions(req):
    # questions = Question.objects.all()
    questions = Question.objects.all()
    data_questions = {"questions": questions}
    return render(req, "polls/question_list.html", data_questions)

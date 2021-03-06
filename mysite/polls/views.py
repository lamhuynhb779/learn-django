from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
# Import Question Form
from .forms import QuestionForm, SendMail
# Import View to use Class base view
from django.views import View

# Create your views here.


# Function base view
# def index(req):
#     # return HttpResponse("Hello cac ban!!!")
#     my_name = 'Lam Huynh'
#     info = ["backend developer", "Love technologies"]
#     return render(req, "polls/index.html", {"name": my_name, "personal": info})


# Class base view
class Index(View):
    # receive request method GET
    @staticmethod
    def get(request):
        my_name = 'Lam Huynh'
        info = ["backend developer", "Love technologies"]
        return render(request, "polls/index.html", {"name": my_name, "personal": info})


def showQuestions(req):
    # Get all
    questions = Question.objects.all()

    # Get by condition
    # Example:
    # get_object_or_404(Question, question_text='Ban thich an gi?', pk = 5)
    # question = get_object_or_404(Question, pk=1)
    # questions = list()
    # questions.append(question)

    data_questions = {"questions": questions}
    return render(req, "polls/question_list.html", data_questions)


def answerForQuestion(req, question_id):
    question = Question.objects.get(pk=question_id)
    choice_list = question.choice_set.all()
    # If use choice_set in template, no need () -> syntax: question.choice_set.all
    return render(req, "polls/answer_question.html", {"question": question, "choices": choice_list})


def saveAnswer(request):
    question = None
    choice_list = list()
    try:
        # Get data to display
        question_id = request.POST["question_input"]
        question = get_object_or_404(Question, pk=question_id)
        choice_list = question.choice_set.all()

        # Get choice and save
        choice_id = request.POST["choice_input"]
        choice = get_object_or_404(Choice, pk=choice_id)

        choice.vote += 1  # increase vote
        choice.save()

        return render(request, "polls/choices.html", {
            "question": question
            , "choices": choice_list
        })

    except Exception as e:
        print(HttpResponse("System have problem: " + str(e)))
        return render(request, "polls/answer_question.html", {
            "question": question
            , "choices": choice_list
        })


def showChoices(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice_list = question.choice_set.all()
    return render(request, "polls/choices.html", {"question": question, "choices": choice_list})


# Model Form
def addQuestion(req):
    # return HttpResponse("Add Question")
    question_form = QuestionForm()

    if req.method == "POST":
        add_question_form = QuestionForm(req.POST)
        if add_question_form.is_valid():
            add_question_form.save()
            return HttpResponse("Insert success!!!")
        else:
            return HttpResponse("Validate failure!!!")

    return render(req, "polls/add_question.html", {"f": question_form})


# Form
# def mail(req):
#     my_mail = SendMail()
#     if req.method == "POST":
#         mail_form = SendMail(req.POST)
#         if mail_form.is_valid():
#             return HttpResponse(mail_form.cleaned_data['email'] + " was sent!!!")
#         else:
#             return HttpResponse('Data mail is invalid. Please check again!!!')
#     return render(req, "polls/mail.html", {"f": my_mail})


class Mail(View):
    @staticmethod
    def get(request):
        my_mail = SendMail()
        return render(request, "polls/mail.html", {"f": my_mail})

    @staticmethod
    def post(self, request):
        mail_form = SendMail(request.POST)
        if mail_form.is_valid():
            return HttpResponse(mail_form.cleaned_data['email'] + " was sent!!!")
        else:
            return HttpResponse('Data mail is invalid. Please check again!!!')

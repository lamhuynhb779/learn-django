from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
# Import Question Form
from .forms import QuestionForm

# Create your views here.


def index(req):
    # return HttpResponse("Hello cac ban!!!")
    my_name = 'Lam Huynh'
    info = ["25 years old", "backend developer", "Love technologies"]
    return render(req, "polls/index.html", {"name": my_name, "personal": info})


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

    return render(req, "polls/add_question.html", {'f': question_form})

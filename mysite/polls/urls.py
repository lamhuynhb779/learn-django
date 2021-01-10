from django.urls import path
from . import views

# This is namespace url
app_name = 'polls_route'

urlpatterns = [
    path('', views.index, name="index"),
    path('questions', views.showQuestions, name="questions"),
    path('questions/<int:question_id>', views.answerForQuestion, name="answer_question"),
    path('questions/save', views.saveAnswer, name="save_answer"),
    path('choices/<int:question_id>', views.showChoices, name="choices"),

    # Model Form
    path('questions/add', views.addQuestion, name="add_question"),

]

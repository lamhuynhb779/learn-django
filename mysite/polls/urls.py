from django.urls import path
from . import views

# This is namespace url
app_name = 'polls_route'

urlpatterns = [
    # Function base view
    # path('', views.index, name="index"),
    # Class base view
    path('', views.Index.as_view(), name="index"),
    path('questions', views.showQuestions, name="questions"),
    path('questions/<int:question_id>', views.answerForQuestion, name="answer_question"),
    path('questions/save', views.saveAnswer, name="save_answer"),
    path('choices/<int:question_id>', views.showChoices, name="choices"),

    # Model Form
    path('questions/add', views.addQuestion, name="add_question"),
    # Form
    # path('mail', views.mail, name="send_mail"),
    path('mail', views.Mail.as_view(), name="send_mail"),
]

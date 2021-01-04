from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    #return HttpResponse("Hello cac ban!!!")
    myname = 'Lam Huynh'
    info = ["25 years old", "backend developer", "Love technologies"]
    return render(req, "polls/index.html", {"name": myname, "personal": info})

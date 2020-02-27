from django.shortcuts import render
from django.http import HttpResponse
from home.models import Login

def index(request):
    return HttpResponse("Hey User!")
    all_users=Login.objects.all()
    html=''
    for users in all_users:
        html+= "Please check in :" + users.username + '<br>'
    return HttpResponse(html)

# Create your views here.

def detail(request, user_id):
    return HttpResponse("You have logged in successfuly dear"+str(user_id))

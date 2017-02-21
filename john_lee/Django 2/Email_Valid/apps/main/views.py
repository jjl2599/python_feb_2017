from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def registration(request):
    user_input = User.objects.valid(request.POST['email'])
    if user_input[0] == False:
        messages.error(request, user_input[1][0])
        return redirect('/')
    else:
        messages.success(request, user_input[1].email)
        return redirect('/registered')

def registered(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'main/success.html', context)

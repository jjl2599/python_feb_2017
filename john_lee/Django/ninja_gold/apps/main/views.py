from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
    if 'result' not in request.session:
        request.session['result'] = []
    return render(request, 'main/index.html')

def display(request):
    if request.method == 'POST':
        print request.POST['building']
        if request.POST['building'] == 'farm':
            num = random.randint(10,20)
            request.session['totalgold'] += num

        elif request.POST['building'] == 'cave':
            num = random.randint(5,10)
            request.session['totalgold'] += num

        elif request.POST['building'] == 'house':
            num = random.randint(2,5)
            request.session['totalgold'] += num

        elif request.POST['building'] == 'casino':
            chance = random.randint(1,2)
            if chance == 1:
                num = random.randint(0,50)
                request.session['totalgold'] += num
            elif chance == 2:
                num = random.randint(-50,0)
                request.session['totalgold'] += num

        if num >= 0:
            event = "Earned"
        elif num < 0:
            event = "Lost"

        str= "{} {} gold from the {}".format(event,abs(num),request.POST['building'])

        request.session['result'].insert(0,str)
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

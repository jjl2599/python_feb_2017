from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def ninja(request, vararg):
	if vararg == "":
		print "hello"
		request.session['img'] = "/../../static/main/images/tmnt.png"
	elif vararg == "blue":
		request.session['img'] = "/../../static/main/images/blue.jpg"
	elif vararg == "orange":
		request.session['img'] = "/../../static/main/images/orange.png"
	elif vararg == "red":
		request.session['img'] = "/../../static/main/images/red.jpg"
	elif vararg == "purple":
		request.session['img'] = "/../../static/main/images/purple.png"
	else:
		request.session['img'] = "/../../static/main/images/april.jpg"
	return render(request, 'main/show.html')

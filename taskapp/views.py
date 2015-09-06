from django.shortcuts import render
from django.http import HttpResponse
from taskapp.models import Task
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def index(request):
	if request.method == 'GET':
		a = Task.objects.all().order_by('date').reverse()
		context ={'tasks':a}
		return render(request,'taskapp/index.html',context)
	elif request.method == 'POST':
		t =  request.POST.get("task", "")
		a = Task(text=t,date=timezone.now())
		a.save()
		return redirect('/')

# Create your views here.

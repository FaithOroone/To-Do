from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import todo
from .forms import todoForm

def index(request):
	todo_list = todo.objects.order_by('id')
	form = todoForm()
	context = {'todo_list' : todo_list, 'form' : form}
	return render(request, 'todo/index.html', context)
@require_POST
def addtodo(request):
	form = todoForm(request.POST)

	if form.is_valid():

		new_todo = todo(text=request.POST['text'])
		new_todo.save()
	return redirect('index')

def completetodo(request, todo_id):
	todo = todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')

def deleteCompleted(request):
	todo.objects.filter(complete__exact=True).delete()
	return redirect('index')

def deleteAll(request):
	todo.objects.all().delete()
	return redirect('index')





   
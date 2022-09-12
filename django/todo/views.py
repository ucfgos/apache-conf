from re import T
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from todo.forms import TodoForm

from . import models

# Create your views here.
@login_required()
def index(req):
    pending_list = models.TodoItem.objects.filter(
        user=req.user,
        done=False
    )
    done_list = models.TodoItem.objects.filter(
        user=req.user,
        done=True
    )

    context = {
        'pending_list': pending_list,
        'done_list': done_list
    }

    return render(req, 'todo/index.html', context)

@login_required()
def get_todo(req, *args, **kwargs):
    todo = models.TodoItem.objects.get(id=kwargs.get('id'))
    form = TodoForm(initial={'title': todo.title, 'description': todo.description})
    return render(req, 'todo/edit.html', {'form': form, 'id': todo.id})

@login_required()
def edit_todo(req, *args, **kwargs):
    form = TodoForm(req.POST)
    if not form.is_valid():
        return render(req, 'todo/edit.html', {'form': form})
    
    todo = models.TodoItem.objects.get(id=kwargs.get('id'))
    todo.title = form.cleaned_data['title'] 
    todo.description = form.cleaned_data['description'] 
    todo.save()

    return redirect('/')

def delete_todo(req, *args, **kwargs):
    todo = models.TodoItem.objects.get(id=kwargs.get('id'))
    todo.delete()
    return redirect("/")
    

@login_required()
def done(req, *args, **kwargs):
    todo = models.TodoItem.objects.get(id=kwargs.get('id'))
    todo.done = True
    todo.save()
    return redirect('/')

class CreateTodo(LoginRequiredMixin, TemplateView):
    template_name='todo/new.html'

    def get(self, req, *args, **kwargs):
        form = TodoForm()
        return render(req, self.template_name, {'form': form})

    def post(self, req, *args, **kwargs):
        form = TodoForm(req.POST)

        if not form.is_valid():
            return render(req, self.template_name, {'form': form})

        models.TodoItem.objects.create(
            title=form.cleaned_data["title"],
            description=form.cleaned_data["description"],
            user=req.user
        )

        return redirect('/')
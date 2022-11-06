from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Task
from .forms import CreateTaskForm


class TaskView(View):
    template_name = "task.html"

    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')

        context = {
            'task': Task.objects.get(id=kwargs['id'])
        }
        return render(request, self.template_name, context)


class CreateTaskView(View):
    template_name = "create_task.html"
    form = CreateTaskForm

    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')

        form = self.form(request.POST)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data)
        return redirect('task_list')


class TaskListView(View):
    template_name = "task_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')

        context = {
            'task_list': Task.objects.all()
        }
        return render(request, self.template_name, context)

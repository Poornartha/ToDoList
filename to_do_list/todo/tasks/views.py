from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Consumer
from .forms import *
# Create your views here.


def index(request, pk):
    task_list = Task.objects.all()
    customer = Consumer.objects.get(id=pk)
    form = NewForm()

    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            title = form.post.get('title')
            completed = False
            customer.Task.objects.create(title, completed)
        return redirect('/')

    context = {
        'task_list': task_list,
        'form': form,
    }
    return render(request, 'tasks/index.html', context)


def update_task(request, cpk, ipk):
    customer = Consumer.objects.get(id=cpk)
    task = customer.Task.objects.get(id=ipk)
    form = NewForm(instance=task)
    context = {
        'task': task,
        'form': form,
    }

    if request.method == "POST":
        form = NewForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, cpk, ipk):
    customer = Consumer.objects.get(id=cpk)
    task = customer.Task.objects.get(id=ipk)
    context = {
        'item': task,
    }

    if request.method == "POST":
        customer.Task.objects.get(id=ipk).delete()
        return redirect("/")

    return render(request, 'tasks/delete_task.html', context)


def home_page(request):
    form = NewCustomer()

    if request.method == "POST":
        form = NewCustomer()
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'tasks/home.html', context)

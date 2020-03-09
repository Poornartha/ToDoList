from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task, Consumer
from .forms import *
# Create your views here.


def index(request, pk):
    customer = Consumer.objects.get(id=pk)
    task_list = customer.task_set.all()
    form = NewForm()

    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            task = form.save()
            customer.task_set.add(task)
        return redirect('index', pk)

    context = {
        'task_list': task_list,
        'customer_id': pk,
        'form': form,
    }
    return render(request, 'tasks/index.html', context)


def update_task(request, cpk, tpk):
    customer = Consumer.objects.get(id=cpk)
    task = customer.task_set.all().get(id=tpk)
    form = NewForm(instance=task)
    context = {
        'customer_id': cpk,
        'task': task,
        'form': form,
    }

    if request.method == "POST":
        form = NewForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, cpk, tpk):
    customer = Consumer.objects.get(id=cpk)
    task = customer.task_set.get(id=tpk)
    print(task)
    task.delete()
    return redirect('index', cpk)


def home_page(request):
    form = NewCustomer()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = NewCustomer(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            customer = Consumer.objects.get(name=name)
            if customer.password == password:
                return redirect('index', customer.pk)
            else:
                return redirect('home')
    return render(request, 'tasks/home.html', context)


def signup_page(request):
    form = NewCustomer()
    if request.method == "POST":
        form = NewCustomer(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'tasks/sign_up.html', context)

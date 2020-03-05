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
            title = form.post.get('title')
            completed = False
            customer.Task.objects.create(title, completed)
        return redirect('index')

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
    task = customer.task_set.all().get(id=tpk)
    context = {
        'item': task,
        'customer_id': cpk,
    }

    if request.method == "POST":
        customer.task_set.all().get(id=tpk).delete()
        return redirect('index', cpk)

    return render(request, 'tasks/delete_task.html', context)


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
            try:
                customer = Consumer.objects.get(name=name)
                if customer.password == password:
                    context = {
                        'task_list': customer.task_set.all(),
                        'customer_id': customer.pk,
                        'form': form,
                    }
                    return redirect('index', customer.pk)
                else:
                    return redirect('home')
            except:
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

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
import pika
import json

def ask_pika(request):
    token = request.COOKIES.get('token')

    credentials = pika.PlainCredentials('user', 'password')

    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
    channel = connection.channel()

    channel.queue_declare(queue='check_auth')

    channel.basic_publish(
        exchange='',
        routing_key='check_auth',
        body=json.dumps({'token': token})
    )
    return None

def index(request):
    ask_pika(request)
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def create(request):
    class TaskForm(ModelForm):
        class Meta:
            model = Task
            fields = '__all__'

    form = TaskForm()
    context = {
        'form': form
    }
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', context)

def edit(request, id):
    instance = get_object_or_404(Task, id=id)
    class TaskForm(ModelForm, ):
        class Meta:
            model = Task
            fields = '__all__'

    form = TaskForm(instance = instance)
    context = {
        'form': form,
        'can_delete': True
    }
    if request.POST:
        if request.POST['delete']:
            instance.delete()
            return redirect('index')
        else:
            form = TaskForm(request.POST, instance = instance)
            if form.is_valid():
                form.save()
                return redirect('index')
    return render(request, 'edit.html', context)
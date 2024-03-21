from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
import pika
import json
from asyncs import *

# def meow(string = 'Meow!'):
#     print('', file=sys.stderr)
#     print(string, file=sys.stderr)
#     print('', file=sys.stderr)

def ask_pika(request):
    token = request.COOKIES.get('token')

    credentials = pika.PlainCredentials('user', 'password')

    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
    channel = connection.channel()

    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue

    global x_response
    x_response = None

    def on_response(ch, method, props, body):
        # meow(str(body))
        global x_response
        x_response = body

    channel.basic_consume(
        queue=callback_queue,
        on_message_callback=on_response,
        auto_ack=True)

    channel.queue_declare(queue='check_auth')

    message = {'token': token}

    validate(instance=message, schema=schema_task_to_auth)
    meow('schema_task_to_auth is good')

    channel.basic_publish(
        exchange='',
        routing_key='check_auth',
        properties=pika.BasicProperties(
            reply_to=callback_queue
        ),
        body= json.dumps(message)
    )

    # THIS IS THE PLACE
    while x_response is None:
        connection.process_data_events(time_limit=None)

    return x_response


def index(request):
    token = request.GET.get('set_token')
    if token:
        response = redirect('http://localhost:8010/') # replace redirect with HttpResponse or render
        response.set_cookie('token', token, max_age=1000)
        return response
    
    pika_response = json.loads(ask_pika(request))
    
    validate(instance=pika_response, schema=schema_auth_to_task)
    meow('schema_auth_to_task is good')

    if pika_response['user_id']:
        pass
    else:
        return redirect('http://localhost:8000/login?back=http://localhost:8010/')

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
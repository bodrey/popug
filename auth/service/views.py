from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
import sys
import random
import string

def meow(string = 'Meow!'):
    print('', file=sys.stderr)
    print(string, file=sys.stderr)
    print('', file=sys.stderr)

def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)

def login(request):
    back = request.GET.get('back')
    class UserForm(ModelForm):
        class Meta:
            model = User
            fields = 'name', 'password'
    form = UserForm()
    context = {
        'form': form
    }
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                name  = request.POST.get("name")
                password = request.POST.get("password")
                user = User.objects.get(name = name, password = password)
                token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
                user.token = token
                user.save()
                meow('good auth')
                return redirect(back + '?set_token=' + token)
            except:
                meow('wrong auth')
    return render(request, 'login.html', context)

def create(request):
    class UserForm(ModelForm):
        class Meta:
            model = User
            fields = '__all__'

    form = UserForm()
    context = {
        'form': form
    }
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', context)

def edit(request, id):
    instance = get_object_or_404(User, id=id)
    class UserForm(ModelForm):
        class Meta:
            model = User
            fields = '__all__'

    form = UserForm(instance = instance)
    context = {
        'form': form,
        'can_delete': True
    }
    if request.POST:
        # if request.POST['delete']:
        #     instance.delete()
        #     return redirect('index')
        # else:
        form = UserForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'edit.html', context)
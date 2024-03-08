from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm

def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)

def login(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)

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
        if request.POST['delete']:
            instance.delete()
            return redirect('index')
        else:
            form = UserForm(request.POST, instance = instance)
            if form.is_valid():
                form.save()
                return redirect('index')
    return render(request, 'edit.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
import pika
import json
from asyncs import *

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)
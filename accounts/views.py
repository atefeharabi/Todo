from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def user_register(request):
    return HttpResponse('hello')
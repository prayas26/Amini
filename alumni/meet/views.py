from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from .models import *
from django.shortcuts import render
from .forms import *

def alumnus(request):
    form = AlumnusForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, "new1.html", context)

def answer(request):
    form = AnswerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
    context = {
        "form1": form1,
    }
    return render(request, "new1.html", context)
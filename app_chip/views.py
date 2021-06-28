from django.shortcuts import render
from django.core.mail import send_mail

from app_chip.models import *
from app_chip.forms import *

# import subprocess

def index(request):
    if request.method == 'GET':
        form = VisitorForm()
        return render(
            request,
            'index.html',
            {'form': form,
            'message': 'This is NOT, a computer generated greeting..'}
            )
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_entry = Visitor.objects.create(
                name=data['name'],
                email=data['email'],
                desc=data['description'],
            )
            send_mail(
                f"Visitor Visited: {data['name']}",
                f"Hey you dumb shit, {data['name']} recently visted. Email them back at {data['email']}",
                f"{data['email']}",
                ['c.pick.coding@gmail.com'],
                fail_silently=False,
                )
            return render(
            request,
            'index.html',
            {'form': VisitorForm(),
            'message': 'Thank you very much, Human.',
            }
        )
        

def resume(request):
    if request.method == 'GET':
        return render(request, 'resume.html')
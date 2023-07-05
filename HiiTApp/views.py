from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject = request.POST.get('Subject')
        message_text = request.POST.get('Message')

        if name and email and subject and message_text:
            message = Message.objects.create(name=name, email=email, subject=subject, message=message_text)
            message.save()
    
    return render(request, 'HiiTApp/index.html')

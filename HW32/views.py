from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            Feedback.objects.create(name=name, message=message)
            return redirect('success')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def home(request):
    return HttpResponse("Welcome to the home page!")

from django.shortcuts import redirect

def redirect_to_feedback(request):
    return redirect('feedback')  # 'feedback' здесь является именем URL-




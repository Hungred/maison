from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})

def detail(request, pk):
    feedbacks = get_object_or_404(CustomerFeedback, pk=pk)
    return render(request, 'feedback_detail.html', {'feedbacks':feedbacks})

def SearchPage(request):
    srh = request.GET['query']
    feedbacks = CustomerFeedback.objects.filter(name__icontains=srh)
    if not feedbacks:
        feedbacks = CustomerFeedback.objects.filter(cometime__icontains=srh)

    params = {'feedbacks': feedbacks, 'search': srh}
    return render(request, 'search_page.html', params)
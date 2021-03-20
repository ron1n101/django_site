from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def teams(request):
    return render(request, 'main/teams.html')

def gallery(request):
    return render(request, 'main/phgallery.html')

def feedback(request):
    return render(request, 'main/feedback.html')

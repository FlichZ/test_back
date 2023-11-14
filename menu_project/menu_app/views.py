from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'menu_app/index.html', context={})

def about_view(request):
    return render(request, 'menu_app/about.html', context={})
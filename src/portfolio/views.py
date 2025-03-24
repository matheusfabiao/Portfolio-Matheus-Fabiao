from django.shortcuts import render

from .models import Category, Project


# Create your views here.
def index(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    context = {'categories': categories, 'projects': projects}
    return render(request, 'portfolio/index.html', context)

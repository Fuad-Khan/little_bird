from django.shortcuts import render
from services.models import Service, Category, Area

def home(request):
    services = Service.objects.filter(is_available=True)[:6]  # show top 6
    categories = Category.objects.all()
    areas = Area.objects.all()
    return render(request, 'core/home.html', {
        'services': services,
        'categories': categories,
        'areas': areas
    })

from django.shortcuts import render
from services.models import Service, Category, Area

def home(request):
    selected_area = request.GET.get('area')
    selected_category = request.GET.get('category')

    services = Service.objects.filter(is_available=True)

    if selected_area:
        services = services.filter(area__id=selected_area)

    if selected_category:
        services = services.filter(category__id=selected_category)

    categories = Category.objects.all()
    areas = Area.objects.all()

    return render(request, 'core/home.html', {
        'services': services,
        'categories': categories,
        'areas': areas,
        'selected_area': int(selected_area) if selected_area else '',
        'selected_category': int(selected_category) if selected_category else '',
    })

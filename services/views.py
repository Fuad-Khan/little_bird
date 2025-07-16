from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import ServiceForm

def staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(staff_check)
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})

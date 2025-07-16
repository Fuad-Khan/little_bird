from django.contrib.auth.decorators import login_required

@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_service.html', {
        'form': form,
        'service': service
    })
def booking_success(request):
    return render(request, 'bookings/success.html')

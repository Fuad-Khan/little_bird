from django.urls import path
from . import views

urlpatterns = [
    path('<int:service_id>/book/', views.book_service, name='book_service'),
    path('success/', views.booking_success, name='booking_success'),
]

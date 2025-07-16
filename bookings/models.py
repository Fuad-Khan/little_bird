from django.db import models
from services.models import Service, Area
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=15)
    special_request = models.TextField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.title} for {self.user.username}"

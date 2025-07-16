from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)  # optional FontAwesome icon
    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    description = models.TextField()
    area = models.ManyToManyField(Area)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

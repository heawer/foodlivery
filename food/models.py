from django.contrib.auth.models import User
from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    cook = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    cook = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
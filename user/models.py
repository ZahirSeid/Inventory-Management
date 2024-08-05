from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default='default.png', upload_to='profile_images')

    def __str__(self):
        return f'{self.employee.username} - Profile'
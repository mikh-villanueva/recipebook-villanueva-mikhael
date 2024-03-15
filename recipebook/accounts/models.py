from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    ShortBio = models.TextField(
        validators = [MinLengthValidator(255, "Short Bio should be more than 255 characters")]
        )
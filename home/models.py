from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
# class User(AbstractUser):
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField(max_length=254)
    
class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chosen_problems")
    image = models.ImageField(upload_to='images')
    image_data = models.BinaryField(null=True)
    latex = models.CharField(max_length=1000, default="Error Generating Problem")
    
class GeneratedProblem(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="generated_problems")
    generated = models.CharField(max_length=1000, default="Error Generating Problem")
    
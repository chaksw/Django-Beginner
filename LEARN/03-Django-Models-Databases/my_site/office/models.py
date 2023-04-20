from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
# Each model class is representing a table
# Each field or attribute inside the model is representing some sort of column inside


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(
        default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])
    # heartrate = models.IntegerField(null=True)
    
    
    # Update exsiting data entryl, and 
    
    # define what information need to print while printign an instance
    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name} is {self.age} years old.'

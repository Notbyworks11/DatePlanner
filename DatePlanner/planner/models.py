from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE)
    preferences = models.TextField(blank=True ,null= True) # Store user preferences as a JSON or tex
    
    def __str__(self):
        return self.user.username
    

#A model to store individual date plans:
class DatePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    
#Models to save favorite places and keep a history of past dates:
class FavoritePlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class DateHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_plan = models.ForeignKey(DatePlan, on_delete=models.CASCADE)
    date_completed = models.DateField()

    def __str__(self):
        return f"{self.date_plan.name} - {self.date_completed} - {self.user.username}"
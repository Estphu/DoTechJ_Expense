from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

TYPE = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative'),
)

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField()
    expense = models.FloatField(default=0)
    balance = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("tracker:home")
       


class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.FloatField(null=True)
    expense_type = models.CharField(max_length=50,choices=TYPE)

    def __str__(self):
        return self.name   

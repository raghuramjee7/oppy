from django.db import models
from django.urls import reverse

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    units = models.IntegerField()

    def __str__(self):
        return self.name

class TradeHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    units = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.TextField() # Options: BUY, SELL
    time = models.DateTimeField(auto_now_add=True)

class Balance(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)

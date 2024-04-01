from django.db import models

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    units = models.IntegerField()
    last_bought = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TradeHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    units = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.TextField() # Options: BUY, SELL
    time = models.DateTimeField(auto_now_add=True)


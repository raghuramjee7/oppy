from django.contrib import admin
from .models import Portfolio, TradeHistory, Balance

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(TradeHistory)
admin.site.register(Balance)

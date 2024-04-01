from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Portfolio, TradeHistory, Balance

# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    

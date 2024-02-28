from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Business

app_name='main'

def about(request):
      return render(request,'home/about.html',{})

def contact(request):
      return render(request,'home/contact.html',{})

def home(request):
      return render(request,'home/home.html',{})

class BusinessListView(ListView):
      model=Business
      template_name='business/business-home.html'
      context_object_name='buss'      

class BusinessCreateView(LoginRequiredMixin, CreateView):
      model=Business
      fields=[
            'name',
            'location',
            'contact',
            'description',
            'link',
            ]
      def form_valid(self, form):
            form.instance.owner=self.request.user
            return super().form_valid(form)

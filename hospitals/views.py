
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Hospital

app_name='hospital'

class BusinessListView(ListView):
      model=Hospital
      template_name='hospital/hospital-home.html'
      context_object_name='hosts'      


class BusinessCreateView(LoginRequiredMixin, CreateView):
      model=Hospital
      fields=[
            'name',
            'location',
            'contact',
            'facility',
            ]
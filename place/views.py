from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Place

app_name='place'

class PlaceListView(ListView):
      model=Place
      template_name='places/places-home.html'
      context_object_name='places'      


class PlaceCreateView(LoginRequiredMixin, CreateView):
      model=Place
      fields=[
            'name',
            'location',
            'highlight',
            ]
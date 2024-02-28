from django.urls import path
from . import views


urlpatterns = [
    path('',views.PlaceListView.as_view(),name='places-home'),   
    path('add/',views.PlaceCreateView.as_view(template_name='places/add-places.html'),name='places-add'),   
    
    ]
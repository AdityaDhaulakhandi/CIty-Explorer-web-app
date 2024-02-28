from django.urls import path
from . import views


urlpatterns = [
    path('',views.BusinessListView.as_view(),name='hospital-home'),   
    path('add/',views.BusinessCreateView.as_view(template_name='hospital/add-hospital.html'),name='hospital-add'),   
    
    ]
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='main-home'),   
    path('business/',views.BusinessListView.as_view(),name='business-home'),   
    path('business/add/',views.BusinessCreateView.as_view(template_name='business/add-business.html'),name='business-add'),   
    
    path('about/',views.about,name='main-about'), 
    path('contact/',views.contact,name='main-contact'), 
    ]
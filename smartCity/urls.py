
from django.contrib import admin
from django.urls import path,include
from account import views as user_view
from django.contrib.auth import views as auth_views

from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/',user_view.register,name='users-register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True),name='users-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='users-logout'),

    path('profile/',user_view.profile,name='users-profile'),
    path('profile/update',user_view.profile_update,name='users-profile-update'),
    # USER ENDS

    path('',include('home.urls')),
    path('hospital/',include('hospitals.urls')),
    path('places/',include('place.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     

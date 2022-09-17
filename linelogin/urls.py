from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'linelogin'

urlpatterns = [
    # path('', social_django.urls,name='logins'),
    # path("logout/", auth_views.LogoutView.as_view(), name='logout'), 
]

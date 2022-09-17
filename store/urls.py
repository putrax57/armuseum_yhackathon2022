from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('mycollections', views.all_stores,name='all_items'),   
    path('<int:itemsno>/', views.details,name='details'),  
    path('transacted/<int:itemsno>/', views.completed,name='completed'),  
    path('buyupdate/<int:itemsno>', views.buyupdate,name='buyupdate'),  
]

from django.urls import path
from . import views  ### esto es lo mismo que--> from myapp import views  

urlpatterns = [
    path('', views.hello),
    path('about/', views.about)
]
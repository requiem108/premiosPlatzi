from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:queston_id>/', views.detail, name="index"), 
    path('<int:queston_id>/results', views.results, name="index"), 
    path('<int:queston_id>/vote', views.vote, name="index"),     
]
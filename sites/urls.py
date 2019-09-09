from django.urls import path
from . import views

app_name = 'sites'

urlpatterns = [
    path('', views.index, name='index'),
    path('themes/', views.themes, name='themes'),
    path('themes/website', views.website, name='website'),
    path('themes/<slug:slug>', views.website_detailed, name='detailed'),
    path('themes/website/new', views.new, name='new'),
]

from django.urls import path
from . import views

app_name = 'sites'

urlpatterns = [
    path('', views.index, name='index'),
    path('themes/', views.themes, name='themes'),
    path('themes/website', views.website, name='website'),
    path('themes/website/<slug:slug>', views.website_detailed, name='detailed'),
    path('themes/website/create/new', views.new, name='new'),
    path('themes/cv', views.cv, name='cv'),
    path('themes/cv/<slug:slug>', views.cv_detailed, name='cv-detailed'),
    path('themes/cv/create/new', views.cv_new, name='cv-new'),
]

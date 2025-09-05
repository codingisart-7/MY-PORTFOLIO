from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('service-details/<str:service_slug_url>', views.service_detail_page, name='service-details'),
    path('portfolio-details/<str:portfolio_slug_url>', views.portfolio_detail_page, name='portfolio-details'),
    
]
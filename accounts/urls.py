from django.conf.urls import url
from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='title_page'), 
    ]
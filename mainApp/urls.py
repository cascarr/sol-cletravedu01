from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepg, name="cletravedu.home"),
    path('enquiry/', views.enquirypg, name="cletravedu.enquiry"),
    path('about-cletrav-education/', views.aboutpg, name="cletravedu.about"),
    path('cletrav-education-news/', views.newspg, name="cletravedu.news"),
]
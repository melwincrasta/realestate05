from django.urls import path
from . import views

urlpatterns = [
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add/', views.add_property, name='add_property'),
    path('<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('<int:pk>/delete/', views.delete_property, name='delete_property'),
    path('', views.home, name='home'),
     path('about/',views.about, name='about'),
     path('contact/',views.contact, name='contact'),
     path('testimonial/',views.testimonial, name='testimonial'),

     
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

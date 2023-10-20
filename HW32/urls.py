from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback'),  # Убедитесь, что имя 'feedback' присутствует
    path('success/', views.success, name='success'),  # Аналогично, убедитесь, что 'success' тоже присутствует
]

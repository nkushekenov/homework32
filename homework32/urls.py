from django.contrib import admin
from django.urls import path, include
from HW32 import views as HW32_views  # Импортируйте модуль views из вашего приложения

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('HW32.urls')),
    path('captcha/', include('captcha.urls')),
    path('', HW32_views.redirect_to_feedback),  # Новый путь для редиректа на страницу обратной связи
]

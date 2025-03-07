from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from food import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('food.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
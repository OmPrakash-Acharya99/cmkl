"""
URL configuration for game_tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Define app_name for both apps
app_name = 'dashboard'
user_app_name = 'user'

# defining views for users
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), # dashboard application
    path('login/', views.login , name = 'login'),
    path('accounts/', include('allauth.urls')),
    path('logout/',views.logout, name = 'logout'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', views.verify_email_complete, name='verify-email-complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
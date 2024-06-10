from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', views.verify_email_complete, name='verify-email-complete'),
]


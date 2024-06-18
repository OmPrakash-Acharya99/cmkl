from django.urls import path
from . import views

urlpatterns = [
    # Path to the base or dashboard
    path('', views.base, name='base'),

    # Path to the home page and it requires login.
    path('home/', views.home, name='home'),
    # urls for notificatiosn
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/read/<int:notification_id>/',views. mark_as_read, name='mark_as_read'),
    # Path to the knowledge page and it requires login.
    path('knowledge/', views.knowledge, name='knowledge'),

    # Path to the courses page and it requires login.
    path('courses/', views.courses, name='courses'),
    path('unreal/', views.unreal, name='unreal'),
    path('photoshop/', views.photoshop, name='photoshop'),

    # Path to the Tools page and it requires login.
    path('tools/', views.tools, name='tools'),
    path('content1/', views.content1, name='content1'),
    path('AI_digital_tools/', views.AI_tools, name='AI_Digital_tools'),

    path('item1/', views.item1, name='item1'),
]

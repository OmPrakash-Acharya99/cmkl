from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .models import Tools, Training_video, Notification
from django.urls import reverse
User = get_user_model()

@receiver(post_save, sender=Tools)
def create_tool_notification(sender, instance, created, **kwargs):
    if created:
        message = f"New tool added: {instance.Title}"
    else:
        message = f"Tool updated: {instance.Title}"
    
    for user in User.objects.all():
        Notification.objects.create(user=user, message=message)

        # Construct the website link
        site_link = reverse('login')  # Assuming 'login' is the URL name for the login page

        # Append the website link to the message
        message_with_link = f"{message}\n\nLogin to view: http://localhost:8000{site_link}"

        send_mail(
            'Tool Notification',
            message_with_link,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

@receiver(post_save, sender=Training_video)
def create_training_video_notification(sender, instance, created, **kwargs):
    if created:
        message = f"New training video added: {instance.Title}"
    else:
        message = f"Training video updated: {instance.Title}"
    
    for user in User.objects.all():
        Notification.objects.create(user=user, message=message)

        # Construct the website link
        site_link = reverse('login')  # Assuming 'login' is the URL name for the login page

        # Append the website link to the message
        message_with_link = f"{message}\n\nLogin to view: http://localhost:8000{site_link}"

        send_mail(
            'Training Video Notification',
            message_with_link,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_tutorial.settings')  # Replace with your project name

application = get_wsgi_application()





def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_tutorial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

from django.contrib.sites.models import Site

# Check if the Site object exists
try:
    site = Site.objects.get(pk=1)
except Site.DoesNotExist:
    site = Site(pk=1)

# Update or set the domain and name
site.domain = 'localhost:8000'  # Assuming your Django development server runs on port 8000
site.name = 'localhost'  # Replace with your site name
site.save()

if __name__ == '__main__':
    main()

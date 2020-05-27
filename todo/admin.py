from django.contrib import admin

from . models import Todo  # Registering my models.

admin.site.register(Todo)
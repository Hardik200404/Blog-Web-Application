from django.contrib import admin
from .models import Profile

# Registering our profile in the admin.
admin.site.register(Profile)
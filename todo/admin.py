from django.contrib import admin
from .models import Dummy

# Optional registration if Dummy model is used
admin.site.register(Dummy)

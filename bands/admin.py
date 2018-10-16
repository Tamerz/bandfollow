from django.contrib import admin

from .models import User, Artist


admin.site.register(User)
admin.site.register(Artist)

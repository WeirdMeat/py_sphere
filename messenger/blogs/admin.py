from django.contrib import admin
from .models import User

class ChatAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, ChatAdmin)

# Register your models here.

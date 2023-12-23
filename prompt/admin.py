from django.contrib import admin
from .models import Prompt, User, Response

class PromptAdmin(admin.ModelAdmin):
    list_display = ('parameters', 'user_id', 'created_at')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_address',)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('prompt_id', 'text',)        

# Register your models here.

admin.site.register(Prompt, PromptAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Response, ResponseAdmin)
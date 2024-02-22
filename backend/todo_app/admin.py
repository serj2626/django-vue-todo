from django.contrib import admin
from .models import TODO

@admin.register(TODO)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('title', 'description', 'is_complete', 'user', 'created_at', 'updated_at', )

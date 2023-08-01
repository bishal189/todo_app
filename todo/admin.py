from django.contrib import admin
from .models import todo
# Register your models here.
class Todoadmin(admin.ModelAdmin):
    list_display=('text_data','is_completed','created_at')
    search_fields=('text_data',)

admin.site.register(todo,Todoadmin)
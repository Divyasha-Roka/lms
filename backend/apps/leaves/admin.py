from django.contrib import admin
from .models import Leave

# Register your models here.
admin.site.register(Leave)
class LeaveModel(admin.ModelAdmin):
     fields = ['user_name','leave_type','leave_balance','from_date', 'to_date','duration','description','leave_status']
     list_filter = ['user_name', 'leave_type', 'duration', 'leave_status' ]
     list_display = fields
     search_fields = ['user_name', 'leave_type', 'duration', 'leave_status']

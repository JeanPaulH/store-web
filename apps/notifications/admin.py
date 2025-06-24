from django.contrib import admin
from apps.notifications.notifications import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'timestamp', 'is_read')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read', 'timestamp')
    
    
    
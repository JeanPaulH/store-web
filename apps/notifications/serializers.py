from rest_framework import serializers
from apps.notifications.notifications import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

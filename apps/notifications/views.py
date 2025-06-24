from django.shortcuts import render
from rest_framework import viewsets
from apps.notifications.notifications import Notification
from apps.notifications.serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


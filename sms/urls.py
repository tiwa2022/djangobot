from django.urls import re_path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from sms.views import SMSView

urlpatterns = [
    re_path(r'^$', csrf_exempt(SMSView.as_view()))
]
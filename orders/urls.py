from django.urls import re_path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from orders.views import OrderView

urlpatterns = [
    re_path(r'^$', OrderView.as_view())
]
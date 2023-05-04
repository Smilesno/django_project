from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^smscode/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view())
]
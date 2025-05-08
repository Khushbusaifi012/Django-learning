from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.display),
    path('time/',views.time),
    path('html/',views.html),
    path('datetime/',views.datetime_info),
    path('index/',views.index)
]
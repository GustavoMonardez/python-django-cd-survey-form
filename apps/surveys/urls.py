from django.conf.urls import url 
from . import views

urlpatterns = [
    url("^$", views.index),
    url("^process$", views.process),
    url("^success$", views.success),
    url("^reset$", views.reset)
]
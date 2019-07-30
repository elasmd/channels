from django.urls import path, include

from api.program import views

urlpatterns = [
    path('',views.Programs.as_view())
]
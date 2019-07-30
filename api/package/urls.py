from django.urls import path, include

from api.package import views

urlpatterns = [
    path('',views.Packages.as_view())
]
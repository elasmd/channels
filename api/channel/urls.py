from django.urls import path, include

from api.channel import views

urlpatterns = [
    path('',views.Channels.as_view()),

]
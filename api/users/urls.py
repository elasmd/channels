from django.urls import path, include

from api.users import views

urlpatterns = [
    path('',views.UserSub.as_view()),
    path('list/', views.AllChannels.as_view())
]
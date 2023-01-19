from django.urls import path
from apps.users.api.api import UserAPIView, user_api_view, user_detail_api_view

app_name ='user'
urlpatterns = [
    path('usuario/',user_api_view , name='user'),
    path('usuario/<int:pk>', user_detail_api_view, name='user_detail')
]
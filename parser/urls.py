from django.urls import path
from .views import UserListView, UserDetailView, UserParserView


app_name = 'parser'

urlpatterns = [
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('', UserParserView.as_view(), name='parse_user'),
]
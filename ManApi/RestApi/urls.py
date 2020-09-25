from django.urls import path
from .views import UserListView, UserListViewApi

app_name = 'ManApi'

urlpatterns = [
    path('', UserListView.as_view()),
    path('status/', UserListViewApi.as_view()),

]

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("token/", obtain_auth_token, name="api-token"),
    path("list/", views.UserListView.as_view(), name="list-user"),
    path("create/", views.UserCreateView.as_view(), name="create-user"),
    path("manage/", views.UserManageView.as_view(), name='manage-user'),
]

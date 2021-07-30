from django.urls import path
# from rest_framework.routers import DefaultRouter
from . import views
urlpatterns = [
    path('todos/', views.ToDoList.as_view(), name='todos_list'),
    path('todos/<int:pk>',
         views.ToDoDetail.as_view(), name='todos_detail'),
]
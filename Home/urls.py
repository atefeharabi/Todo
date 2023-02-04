from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:todo_id>/', detail, name='details'),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('update/<int:todo_id>/', update, name='update'),
    path('create/', create, name='create'),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('todos', todosView, name='todos'),
    path('delete/<uuid:id>', deleteTodo, name='deleteTodo'),
    path('contact', contactView, name='contact'),
]
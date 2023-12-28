from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('notes/create', views.noteCreate.as_view(), name="noteCreate"),
    path('notes/list', views.noteList.as_view(), name="noteList"),
    path('notes/update/<pk>', views.noteUpdate.as_view(), name="noteUpdate"),
    path('notes/delete/<pk>', views.noteDelete.as_view(), name="noteDelete"),
]
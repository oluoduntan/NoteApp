from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name='index'),
    path('notes/', views.NoteList.as_view(), name="notes"),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name="note"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root, name='index'),
    path('notes/', views.NoteList.as_view(), name="notes"),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name="note"),
    path('user/', views.UserDetail.as_view(), name='user'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
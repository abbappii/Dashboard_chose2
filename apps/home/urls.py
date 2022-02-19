from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    path('', views.index, name='home'),
    path('user-create/', views.user_create, name='user-create'),
    path('roles/', views.roles_for_adm, name='roles'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]

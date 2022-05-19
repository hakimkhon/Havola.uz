from django.urls import path
# from .views import  home
from .views import * 

app_name = "link"

urlpatterns = [
    path("", home, name="home"),
    path("listlar", link_list, name="link_list"),
    path("listlar/create/", link_create, name="link_create"),
    path("listlar/<int:pk>/", link_detail, name="link_detail"),
    path("listlar/<int:pk>/update/", link_update, name="link_update"),
]


from django.contrib import admin
from django.urls import path, include
from links.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('links.urls', namespace = "link")),
    # path('register', register),
    path('users/', include('users.urls', namespace = "users")),
]

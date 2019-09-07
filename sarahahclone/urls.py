
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('userdata.urls')),
    path('user/admin/', admin.site.urls),
]

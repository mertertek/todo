from django.contrib import admin
from django.urls import path, include
from todoapp import urls as todoapp_urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include(todoapp_urls)),
    path('api-auth/', include('rest_framework.urls')),
]

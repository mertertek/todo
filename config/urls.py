from django.contrib import admin
from django.urls import path, include
from todoapp import urls as todoapp_urls  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include(todoapp_urls))  # Include the URLs from the todoapp
]

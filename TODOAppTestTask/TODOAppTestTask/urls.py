from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

urlpatterns = [
    path('api/v1/', include([
        path('admin/', admin.site.urls),
        path('tasks', include('todo_tasks.urls')),
        path('auth/login/', views.obtain_auth_token)
    ]))
]

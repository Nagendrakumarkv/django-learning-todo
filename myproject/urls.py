from django.contrib import admin
from django.urls import path
from tasks.views import task_list, create_task # <--- Update imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'), # Empty string '' means the homepage
    path('create/', create_task, name='create_task'), # <--- Add this
]
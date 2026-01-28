from django.contrib import admin
from django.urls import path
from tasks.views import task_list, create_task, update_task, delete_task  # <--- Update imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('update/<int:pk>/', update_task, name='update_task'), # <--- Dynamic ID
    path('delete/<int:pk>/', delete_task, name='delete_task'), # <--- Dynamic ID
]
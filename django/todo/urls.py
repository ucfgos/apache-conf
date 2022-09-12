from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='todo-index'),
    path('todo/<int:id>', views.get_todo, name='todo-get'),
    path('todo/new', views.CreateTodo.as_view(), name="todo-new"),
    path('todo/<int:id>/edit', views.edit_todo, name='todo-edit'),
    path('todo/<int:id>/done', views.done, name='todo-done'),
    path('todo/<int:id>/delete', views.delete_todo, name='todo-delete')
]
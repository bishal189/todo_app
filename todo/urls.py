
from django.urls import path
from . import views

urlpatterns = [
   
    path('add_task/',views.add_task ,name='add_task'),
    # for completed
    path('completed/<int:pk>',views.complete ,name='complete'),
    # for uncompleted
    path('uncompleted/<int:pk>',views.uncomplete ,name='uncomplete'),

    # for edit task

    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),

    # for delete

    path('delete/<int:pk>',views.delete,name='delete')


]

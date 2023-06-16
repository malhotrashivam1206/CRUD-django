from django.urls import path
from .views import create_note, update_note, delete_note, read_all_notes, read_note_by_id

urlpatterns = [
    path('create/', create_note, name='create'),
    path('update/<int:note_id>/', update_note, name='update'),
    path('delete/<int:note_id>/', delete_note, name='delete'),
    path('read_all/', read_all_notes, name='read_all'),
    path('read/<int:note_id>/', read_note_by_id, name='read'),
]

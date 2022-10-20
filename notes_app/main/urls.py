from django.contrib import admin
from django.urls import path

from notes_app.main.views import show_home, add_note, edit_note, delete_note, details_note, show_profile, \
    create_profile, delete_profile

urlpatterns = (
    path('', show_home, name='show home'),

    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)


''' 
http://localhost:8000/ - home page

http://localhost:8000/add - add note page
http://localhost:8000/edit/:id - edit note page
http://localhost:8000/delete/:id - delete note page
http://localhost:8000/details/:id - note details page

http://localhost:8000/profile - profile page
'''
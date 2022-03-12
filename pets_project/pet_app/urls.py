from django.contrib import admin
from django.urls import path

from pets_project.pet_app.views import home, dashboard, profile_details, photo_details, create_profile, edit_profile, \
    delete_profile, pet_add, pet_edit, pet_delete, photo_add, photo_edit, not_found, photo_delete, like_pet_photo

urlpatterns = [
    path('', home, name='home'),

    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_details, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', pet_add, name='add pet'),
    path('pet/edit/<int:pk>/', pet_edit, name='edit pet'),
    path('pet/delete/<int:pk>/', pet_delete, name='delete pet'),

    path('photo/details/<int:pk>/', photo_details, name='photo details'),
    path('photo/add', photo_add, name='add photo'),
    path('photo/edit/<int:pk>/', photo_edit, name='edit photo'),
    path('photo/delete/<int:pk>/', photo_delete, name='delete photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like photo'),

    path('not-found/', not_found, name='not found'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<slug:slug>", views.room, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("myrooms/", views.my_rooms, name="my_rooms"),
    path("rooms/<int:room_id>/delete/", views.delete_room, name="delete_room"),
]

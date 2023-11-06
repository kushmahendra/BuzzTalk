from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import RoomCreationForm
from django.contrib import messages


from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def delete_room(request, room_id):
    room = get_object_or_404(MyRoom, id=room_id)

    if request.user == room.user:
        if request.method == "POST":
            room.delete()
            return redirect("my_rooms")  # Redirect to the list of user's rooms

    return render(request, "delete_room.html", {"room": room})


def my_rooms(request):
    user = request.user
 
    rooms = MyRoom.objects.filter(user=user)
    
    return render(request, "rooms/myrooms.html", {"rooms": rooms})


@login_required(login_url="login")
def rooms(request):
    if request.method == "POST":
        room_code = request.POST.get("join_code")
        room_name = request.POST.get("room_name")

        try:
            room = MyRoom.objects.get(name=room_name, slug=room_code)
            return redirect("/rooms/" + str(room.slug))
        except MyRoom.DoesNotExist:
            messages.error(request, "Wrong code!")

    rooms = MyRoom.objects.all()
    return render(request, "rooms/rooms.html", {"rooms": rooms})


@login_required(login_url="login")
def room(request, slug):
    room = MyRoom.objects.get(slug=slug)
    messages = Messages.objects.filter(room=room)[:25]
    return render(request, "rooms/room.html", {"rooms": room, "messages": messages})


def create_room(request):
    if request.method == "POST":
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            room = form.save(
                commit=False
            )  # Create the room instance but don't save it to the database yet
            room.user = request.user  # Set the user to the logged-in user
            room.save()  # Now save the room to the database
            return redirect("rooms")
    else:
        form = RoomCreationForm()
    return render(request, "rooms/create_room.html", {"form": form})

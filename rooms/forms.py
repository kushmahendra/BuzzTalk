from django import forms
from .models import *


class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = MyRoom
        fields = ["name", "slug"]
        labels = {
            "name": "Room Name",
            "slug": "Room Code",
        }

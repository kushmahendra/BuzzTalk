from django.shortcuts import redirect, render
from django.contrib.auth import login
from .forms import SignupForm


# Create your views here.
def home(request):
    return render(request, "core/index.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "core/signup.html", {"form": form})

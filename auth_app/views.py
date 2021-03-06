from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitteruser_app.models import TwitterUser
from auth_app.forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(username=data.get("username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("home"))
    form = SignUpForm()
    return render(request, "generic.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
    form = LoginForm()
    return render(request, "generic.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm  # Import the LoginForm


# Create your views here.


class TestView(TemplateView):
    template_name = 'home.html'


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid Credentials!")
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, "home.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('home')

    # Redirect to a success page.


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Sign up successful!"))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, "home.html")

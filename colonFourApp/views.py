from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class TestView(TemplateView):
    template_name = 'home.html'


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid Credentials!"))
            redirect('login')
    else:
        return render(request, "home.html")


def logout_view(request):
    logout(request)
    # Redirect to a success page.

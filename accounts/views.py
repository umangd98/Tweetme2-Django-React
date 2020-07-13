from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
def login_view(request, *args, **kwargs):
  form = AuthenticationForm(request, data=request.POST or None)
  if form.is_valid():
    user = form.get_user()
    login(request, user)
    return redirect("/")
  context = {
    "title": "Login",
    "form": form,
    "btn_label": "Login"
  }
  return render(request, "accounts/auth.html", context)

def logout_view(request, *args, **kwargs):
  if request.method == "POST":
    logout(request)
    return redirect("/login")
  context = {
    "title": "Logout",
    "description": "Are you sure you want to logout?",
    "form": None,
    "btn_label": "Click to confirm"
  }
  return render(request, "accounts/auth.html",context)

def registration_view(request, *args, **kwargs):
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    user = form.save(commit=True)
    user.set_password(form.cleaned_data.get("password1"))
    # print(form.cleaned_data)
    login(request, user)
    return redirect("/")
  context = {
    "title": "Register",
    "form": form,
    "btn_label": "Register"
  }
  return render(request, "accounts/auth.html", context)
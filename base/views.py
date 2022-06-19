from django.shortcuts import render, redirect
from .forms import registerform
from .models import card
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
            form = registerform()
    return render(request, "base/register.html", {"form":form})
    
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "base/login.html", {
            "massage": "invalid credentials"
            })
    return render(request, ("base/login.html"))
    

def logout_view(request):
    logout(request)
    return render(request, "base/login.html", {
    "message":"Logged out"
    })


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']
        user = request.user
        all = card(user=user, question=question, answer=answer)
        all.save()
    else:
        pass
    cards = card.objects.filter(user=request.user)
    return render(request, ('base/home.html'), {
   'card': cards
    })
    

def delete(request, pk):
    item = card.objects.get(id = pk)
    item.delete()
    return redirect('home')
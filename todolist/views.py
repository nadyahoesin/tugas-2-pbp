from xxlimited import Null
from todolist.models import Task
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
import datetime

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    try:
        data_task = Task.objects.get(user=request.user)
    except:
        data_task = False

    context = {
        'tasks': data_task,
        'username': request.user.username
    }
    return render(request, "todolist.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            # return redirect('wishlist:show_wishlist')
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    pass

def logout_user(request):
    logout(request)
    # return redirect('wishlist:login')
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
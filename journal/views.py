from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from .forms import CreateUserForm
from django.shortcuts import render, redirect

# Login imports
from .forms import LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout 

# Protect views
from django.contrib.auth.decorators import login_required

@login_required(login_url="my_login")
def dashboard(request):
    return render(request,"dashboard.html")


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        # Different from other we need to pass 
        # request and data is request.POST 
        form = LoginForm(request,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Will check whether the username and password
            # is same with the database and what user entered
            user = authenticate(request, username= username, password=password)
            if user is not None:
                # authorize the user to login
                auth.login(request,user)
                return redirect('dashboard')
    context = {'form':form}
    return render(request, "my-login.html", context)

def user_logout(request):
    auth.logout(request)
    return redirect("my_login")

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    context = {'form':form}
    return render(request, 'register.html', context)
        
def success(request):
    return render(request,'success.html')


def create_task(request):
    form_dict = TaskForm()
    # Check whether the request method is POST in template after submit
    if request.method == 'POST':
        form_dict = TaskForm(request.POST)
        if form_dict.is_valid():
            form_dict.save()
            return redirect('task')
    context = {'form': form_dict}
    return render(request,'create-task.html', context)

# update task
def update_task(request, pk):
    # Get the task which you need to update
    task = Task.objects.get(id=pk)
    # Populate the form with old task details
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')
    context = {'form': form}
    return render(request, 'update-task.html', context)

def delete_task(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task')
    return render(request, 'delete-task.html')

# Return all tasks
def task(request):
    queryAllData = Task.objects.all()
    print(queryAllData)
    context = {'tasks': queryAllData}
    return render(request, 'task.html', context)

def filter_task(request):
    queryData = Task.objects.filter(title="oo")
    for i in queryData:
        print(i.title)
    context = {'tasks': queryData}
    return render(request, 'filter-task.html', context)

# Create your views here.
def home(request):
    # context = {'name':first_name}
    #Passing the client list dictionary
    return render(request,'index.html')



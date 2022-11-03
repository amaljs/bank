from django.shortcuts import render, redirect
from .models import City,Branches
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from .forms import CustomUserForm,TaskForm



def home(request):
    return render(request, 'index.html')


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home/form/')
        else:
            messages.info(request, 'Invalid login')
            return redirect('/home/login/')
    return render(request, 'login.html')


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            # User.objects.create(**form.cleaned_data)
            form.save()
            messages.info(request, 'usercreated')
            print('user created')
            return redirect('/home/login/')

    return render(request, 'user_creation.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/home/')


def finaltask(request):
    form = TaskForm()

    print(request)
    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES)
        f=request.POST.get('material')
        print(f)

        if form.is_valid():

            form.save()
            print('form saved')
            messages.success(request, 'Application Accepted.')
            return render(request,'final.html',{'form':form.cleaned_data})
        else:
            print(form.errors)

    return render(request,'final_form.html',{'form':form})
    #

def load_cities(request):
    branch_id = request.GET.get('branch_id')
    print(branch_id)
    cities = City.objects.filter(branch_id=branch_id)
    return render(request,'city_dropdown_list_options.html', {'cities': cities})

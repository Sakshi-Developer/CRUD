from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import customerform
from .models import customer


from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    form= customerform()
    data= customer.objects.filter(userid= request.user.id).values()
    if request.method=="POST":

            form= customerform(request.POST, request.FILES)
            if form.is_valid():
                form.save()

            # context= {'data': list(data)}
            return JsonResponse(list(data), safe=False)

    context={'data': data}
    return render(request, 'testapp/index.html', context)

@login_required
def edit(request, id):
     data= customer.objects.get(id= id)
     context= {'customer': data}
     return render(request, 'testapp/update.html', context)


def update(request):
    id= request.POST.get('id')
    data= customer.objects.get(id=id)
    print(request.POST)
    form= customerform(request.POST, request.FILES, instance=data)
    form.save()
    return redirect('home')




def deleteData(request, id):
    data= customer.objects.get(id= id)
    data.delete()
    return redirect('home')

def SignUp(request):
    context={}
    if(request.method=="POST"):
        name= request.POST.get('name')
        email= request.POST.get('email')
        password= request.POST.get('password1')

        data= User.objects.create_user(username=name, email=email, password=password)
        data.save()
        context={'msg': 'Account Created Successfully. Please Login'}

    return render(request, 'testapp/signup.html', context)

def Login(request):
     
    context={}
    if request.method=="POST":
        un= request.POST.get('username')
        pw= request.POST.get('password')

        userdata= authenticate(username=un, password=pw)
        if userdata is not None:
             login(request, userdata)
             return redirect('home')
        else:
             context={'msg': 'Invalid Username or Password'}


    return render(request, 'testapp/login.html', context)
    

def logoutuser(request):
     logout(request)
     return redirect ('login')


def base(request):
     return render(request, 'testapp/base.html')


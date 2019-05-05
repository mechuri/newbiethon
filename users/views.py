from django.shortcuts import render , redirect , get_object_or_404
#from .models import User
from django.contrib.auth.models import User

#filter

# Create your views here.
def users(request):
    return render(request,'users/users.html')


def login(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        users = User.objects.all()
        
        for user in users:
            if name == user.username:
                if password == user.password:
                    return render(request,'users/login.html',{'user':user})
        return render(request,'users/login_fail.html')
        

def sign_in(request):
    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        users = User.objects.all()
        
        for user in users:
            if name == user.username:
                return render(request, 'users/sign_in_fail.html')
        
        user = User(username=name,password=password)
        
        user.save()
        return redirect('main')
    return render(request,'users/sign_in.html')
from django.shortcuts import render , redirect , get_object_or_404
#from .models import User
from .m import User

#filter

# Create your views here.
def users(request):
    return render(request,'users/users.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        users = User.objects.all()
        
        for user in users:
            if name == user.name:
                if password == user.password:
                    return render(request,'users/login.html')
        
        return render(request,'users/login_fail.html')
        

def sign_in(request):
    if request.method=="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        lang = request.POST.get('lang')
        interest = request.POST.get('interest')
        atmosphere = request.POST.get('atmosphere')
        email = request.POST.get('email')
        introduce = request.POST.get('introduce')
        
        users = User.objects.all()
        
        for user in users:
            if name == user.name:
                return render(request, 'users/sign_in_fail.html')
        
        user = User(name=name,password=password,gender=gender,lang=lang,interest=interest,atmosphere=atmosphere, email=email, introduce=introduce)
        
        user.save()
        return redirect('main')
    return render(request,'users/sign_in.html')
    
    
    
from django.shortcuts import render , redirect , get_object_or_404
#from .models import User
from .models import User
import pdb

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
                    return render(request,'users/login.html',{'users':user})
     
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
        main_image = request.FILES.get('main_image')

        users = User.objects.all()
        
        for user in users:
            if name == user.name:
                return render(request, 'users/sign_in_fail.html')
        
        user = User(name=name,password=password,gender=gender,lang=lang,interest=interest,atmosphere=atmosphere, email=email, introduce=introduce, main_image=main_image)
        user.save()
        return redirect('main')
    return render(request,'users/sign_in.html')
    

def password(request, id):
    user = User.objects.get(pk=id)
    return render(request,'users/password.html',{'user':user})
    

def check(request):
    if request.method == "POST":
        password = request.POST.get('password')
        check_password = request.POST.get('check_password')
        check_pk = request.POST.get('check_pk')
        user = User.objects.get(pk=int(check_pk))
        # pdb.set_trace()
        if password == check_password:
            return render(request,'users/mypage.html',{'user':user})
    return render(request, 'users/password.html')
    


def mypage(request, id):
    return render(request,'users/mypage.html')

def bye(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        user.delete()
        return redirect('quit')
        
def quit(request):
    return render(request,'users/quit.html')
    
    
def update(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        name = request.POST.get('name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        lang = request.POST.get('lang')
        interest = request.POST.get('interest')
        atmosphere = request.POST.get('atmosphere')
        email = request.POST.get('email')
        introduce = request.POST.get('introduce')
        main_image = request.FILES.get('main_image')
        
        user.name = name
        user.gender = gender
        user.lang = lang
        user.interest = interest
        user.atmosphere = atmosphere
        user.email = email
        user.introduce = introduce
        user.main_image = main_image
        user.save()
    return redirect('main')



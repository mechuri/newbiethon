from django.shortcuts import render, redirect
from users.models import User
import operator
# Create your views here.

def match(request):
    if request.method == "POST":
        gender=request.POST.get('gender')
        lang=request.POST.get('lang')
        interest=request.POST.get('interest')
        atmosphere=request.POST.get('atmosphere')
        
        information = User.objects.all()
        ids = []
        for item in information:
            point = 0
            if gender == item.gender:
            
                if lang == item.lang:
                    if interest == item.interest:
                        point +=1
                    if atmosphere == item.atmosphere:
                        point +=1
                    if point >= 1:
                        ids.append(item.id)
        
        if ids == []:
            return render(request,'fail.html')
        users = User.objects.filter(id__in=ids)
        current_user = request.user.id
        uids = []
        for i in users:
            uids.append(i.id)
        urlss = []
        for i in uids:
            if i > current_user:
                urlss.append(str(current_user)+"_"+str(i))
            else:
                urlss.append(str(i)+"_"+str(current_user))
            
        
        return render(request,'complete.html',{'users':zip(users,urlss)})
    return render(request, 'match.html')
        
    
def complete(request):
    return render(request, 'complete.html')
    

def fail(request):
    return render(request, 'fail.html')
    
    
def all_users(request):
    users = User.objects.all()
    print(request.user)
    return render(request, 'all_users.html', {'users': users})
    
def send_index(request):
    users = User.objecs.all()
    return render(request,'room.html',{'users':users})
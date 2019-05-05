from django.shortcuts import render, redirect
from users.models import User

# Create your views here.

def match(request):
    if request.method == "POST":
        gender=request.POST.get('gender')
        lang=request.POST.get('lang')
        interest=request.POST.get('interest')
        atmposphere=request.POST.get('atmposphere')
        match=[]
        match.insert(0, gender)
        match.insert(1, lang)
        match.insert(2, interest)
        match.insert(3, atmposphere)
        
        user=[]
        user.insert(0, gender)
        user.insert(1, lang)
        user.insert(2, interest)
        user.insert(3, atmposphere)
        

        
        return redirect('complete')
    return render(request, 'complete.html')
        
    
def complete(request):
    print("s")
    
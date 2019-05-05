from django.shortcuts import render

def main(request):
    return render(request,'main.html')
    
    
def main_e(request):
    return render(request,'main-english.html')
    

def main_c(request):
    return render(request,'main-chinese.html')
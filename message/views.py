from django.shortcuts import render

def message(request):
    return render(request,'message/message.html')
    
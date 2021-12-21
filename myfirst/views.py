from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')    

def header(request):
    return render(request,'header.html')    

def footer(request):
    return render(request,'footer.html') 

def contact(request):
    return render(request,'contact.html') 

def helpus(request):
    return render(request,'help.html')                
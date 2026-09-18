from django.shortcuts import render

# Create your views here.
def vista3(request):
    return render(request,"app2/vista3.html")

def vista4(request):
    return render(request,"app2/vista4.html")
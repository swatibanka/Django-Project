from django.shortcuts import render

# Create your views here.
def showIndex(request):
    emp_info = {"idno":101,"name":"ravi","salary":185000.00}
    return render(request,"main.html",emp_info)

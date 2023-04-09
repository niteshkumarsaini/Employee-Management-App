from django.shortcuts import render,redirect
from django.http import HttpResponse
from emp.models import Employee
# Create your views here.
def home(request):
    emps=Employee.objects.all()
    return render(request,"emp/employee.html",{"emp_data":emps})

def add(request):
    if(request.method=="POST"):
       name=request.POST.get("emp-name")
       gender=request.POST.get("emp-gender")
       mobile=request.POST.get("emp-mobile")
       address=request.POST.get("emp-address")
       working=True if request.POST.get("emp-working")=="on" else False
       department=request.POST.get("emp-department")
       e1=Employee(name=name,gender=gender,mobile=mobile,address=address,department=department,working=working)
       e1.save()
       print(name,gender,mobile,address,working,department)
       return redirect('/employee/')
    return render(request,'emp/add.html',{})
def delete(request,emp_id):
    delete_emp=Employee.objects.get(pk=emp_id)
    delete_emp.delete()
    return redirect("/employee/")
def update(request,emp_id):
    emp_update=Employee.objects.get(pk=emp_id)
    return render(request,"emp/update.html",{"data":emp_update})
def updated(request,emp_id):
    do_update=Employee.objects.get(id=emp_id)
    do_update.name=request.POST.get("emp-name")
    do_update.gender=request.POST.get("emp-gender")
    do_update.mobile=request.POST.get("emp-mobile")
    do_update.address=request.POST.get("emp-address")
    do_update.working=True if request.POST.get("emp-working")=="on" else False
    do_update.department=request.POST.get("emp-department")
    do_update.save()
    return redirect('/employee/')
from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

# Inserts the employee information
def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'star/Insert.html',{'form':form})

# Shows the employees information
def show_view(request):
    employees = Employee.objects.all()
    return render(request, 'star/show.html',{'employees':employees})

# Delete the particular employees information
def delete_view(request,id):
    employees = Employee.objects.get(id = id)
    employees.delete()
    return redirect('/')

# updates the particular employees information
def update_view(request,id):
    employees = Employee.objects.get(id = id)
    form = EmployeeForm(request.POST,instance=employees)
    if request.method =='POST':
        form = EmployeeForm(request.POST, instance=employees) 
        if form.is_valid():
            form.save()
            return redirect('/') 
    return render(request,'star/update.html',{'employees':employees})

# Search the particular employee information with Employee Id
def search_view(request):
    query = request.GET['query']
    employees = Employee.objects.filter(Employee_Id__icontains=query)

    single_employee = {'employees':employees}
    return render(request, 'star/search.html', single_employee)

# Shows the salary information
def salary_view(request):
    employees = Employee.objects.all()
    return render(request, 'star/salary.html',{'employees':employees})
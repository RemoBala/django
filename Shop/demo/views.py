from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Person
# Create your views here.
def demo(request):
    return HttpResponse('<h1> hii</h1>')
def form(request):
    return render(request,"form.html")
    

from .forms import MemberForm   
def create_data(request):
    if request.method == 'POST':
        data = request.POST
        
        firstname=data['firstname']
        lastname =data['lastname']
        email=data['email']
        phno=data['phno']
        Date = data['Date']
        print(data)
        Person.objects.create(firstname=firstname,lastname=lastname,email=email,phno=phno,Date=Date)
          
        return redirect('/create') 
    
    return render(request,"create.html")




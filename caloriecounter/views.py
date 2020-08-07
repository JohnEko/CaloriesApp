from django.shortcuts import render, redirect
from .models import Food
from .forms import AddFood

# Create your views here.

def home(request):
    user = Food.objects.all()
    form = AddFood()

    context = { 'user' : user,
                'form'  :form
    }

    return render(request, "caloriecounter/calorie.html", context)

def add(request):
    
    if request.method == 'POST':
        form = AddFood(request.POST or None)
        if form.is_valid():
            form.save()
        
        return redirect("home")
    
    form = AddFood()
    context = { 'form' : form}
    return render(request,"caloriecounter/calorie.html", context )

def nutrition(request, obj):
    users = Food.calories(id=obj)
    count = 0
    if request.method == 'POST':
        for value in users:
                count += value
                return count 

    context = {"users" : users}
    return render(request, "caloriecounter/calorie.html", contex)
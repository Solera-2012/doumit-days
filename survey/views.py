from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from survey.models import Family, FamilyForm
import survey.services as services

from django.db.models import Sum

def home(request):
    fam_form = FamilyForm()
    results=Family.objects.all()
    return render(request, 'home.html', {'results':results, 'fam_form':fam_form})

def submit(request):
    results = Family.objects.all()
    fam_form = FamilyForm()
    if request.method == 'POST':
        form = FamilyForm(request.POST)

        if form.is_valid():
            form.save()
            results = Family.objects.all()
            return render(request, 'home.html', {'results':results,'fam_form':fam_form,'thanks':1})
        else:
            print("Form is not valid! Fields are missing")
            return render(request, 'home.html', {'results':results,'fam_form':form,'thanks':0})
    
    return render(request, 'home.html', {'results':results,'fam_form':fam_form,'thanks':0})


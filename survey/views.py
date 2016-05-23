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
    if request.method == 'POST':
        form = FamilyForm(request.POST)

        if(not form.is_valid()):
            results=Family.objects.all()
            #return render(request, 'home.html', {'fam_form':form, 'results':results})
        else:
            pass
            #new_family = form.save()

            #for i, option in enumerate(Choice.objects.all()):
            #    res = request.POST['c_%s'%(i+1)]
            #    score = Score(family=new_family,choice=option, result=res)
            #    score.save()
    fam_form = FamilyForm()
    
    
    return render(request, 'home.html', {'results':results, 'fam_form':fam_form, 'thanks':1})


from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from survey.models import Family, FamilyForm, Choice, Score
import survey.services as services

from django.db.models import Sum
def home(request):
	fam_form = FamilyForm()
	choices = Choice.objects.all()
	return render(request, 'home.html', {'fam_form':fam_form, 'choices':choices})

def results(request):
    scores = services.summarize_results()
    results=Family.objects.all()

    # TODO: refactor this
    result_data = []
    for choice in Choice.objects.all():
        choice_results=Score.objects.filter(choice=choice).values("result").annotate(total=Sum("family__num_members"))
        in_data=[["Result", "Total"]]
        for c in choice_results:
            in_data.append([c['result'],c['total']])

        result_data.append(in_data)

    return render(request, 'thanks.html', 
        {'results':results, 'scores':scores, 'pie_data': result_data})

def submit(request):
    if request.method == 'POST':
        form = FamilyForm(request.POST)

        if(not form.is_valid()):
            choices = Choice.objects.all()
            return render(request, 'home.html', {'fam_form':form, 'choices':choices})
        else:
            new_family = form.save()

            for i, option in enumerate(Choice.objects.all()):
                res = request.POST['c_%s'%(i+1)]
                score = Score(family=new_family,choice=option, result=res)
                score.save()

    return redirect('/results', request) 

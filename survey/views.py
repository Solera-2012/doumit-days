from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from survey.models import Family, FamilyForm, Choice, Score
from survey.data_processing import summary


def home(request):
	fam_form = FamilyForm()
	choices = Choice.objects.all()
	return render(request, 'home.html', {'fam_form':fam_form, 'choices':choices})


def submit(request):
	if request.method == 'POST':
		form = FamilyForm(request.POST)

		if form.is_valid():
			new_family = form.save()
		
			for i, option in enumerate(Choice.objects.all()):
				res = request.POST['c_%s'%(i+1)]
				score = Score(family=new_family,choice=option, result=res)
				score.save()


	
	scores = summary.process()



	results = Family.objects.all()
	return render(request, 'thanks.html', {'results':results, 'scores':scores})

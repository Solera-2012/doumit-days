from survey.models import Choice, Score, Family
from django.db.models import Sum

def summarize_results():
	scores=Score.objects.all()
	choices=Choice.objects.all()
	families=Family.objects.all()
	
	aggregates=Score.objects.values("choice", "result").annotate(total=Sum("family__num_members"))
	return aggregates


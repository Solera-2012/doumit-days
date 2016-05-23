from survey.models import Family
from django.db.models import Sum


def summarize_by_choice():
    return summarize_results(["choice"])
 
def summarize_by_result():
    return summarize_results(["result"])     

def summarize_results(byVar=["choice", "result"]):
	aggregates=Score.objects.values(*byVar).annotate(total=Sum("family__num_members"))
	return aggregates


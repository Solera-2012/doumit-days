from survey.models import Choice, Score, Family


def process():
	scores=Score.objects.all()
	choices=Choice.objects.all()
	families=Family.objects.all()
	raw_scores = []
	for s in scores:
		raw_scores.append(s.result)

	#this needs to be reworked with built in QuerySet constructs. 
	#there must be a way to do groupBy
	
	byCruise=[]
	for cruise in choices:
		cru = Score.objects.filter(choice=cruise)
		byCruise.append( [(res.family.num_members, res.result, res.choice.name) \
						for res in cru])

	final_scores=[]
	response_types = ('best', 'can', 'cant')
	for cruise in byCruise:
		for response in response_types:
			scs = [a[0] for a in cruise if a[1]==response]
			final_scores.append((sum(scs), response, cruise[0][2]))
	return final_scores





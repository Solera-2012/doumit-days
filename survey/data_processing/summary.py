from survey.models import Choice, Score, Family


def process():
	scores=Score.objects.all()
	
	raw_scores = []
	for s in scores:
		raw_scores.append(s.score)
	
	return raw_scores





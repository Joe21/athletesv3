from django import forms
from athletesproject.apps.athletesapp.models import Athlete

class AthleteForm(forms.ModelForm):
	RECOMMENDATIONS = (
		('a', 'Hire Joe IMMEDIATELY!'),
		('b', 'Hire Joe NOW!')
		)
	first_name = forms.CharField(max_length=50, help_text="First name:")
	last_name = forms.CharField(max_length=50, help_text="Last name:")
	sport = forms.CharField(max_length=50, help_text="Sport:")
	recommendation = forms.ChoiceField(choices=RECOMMENDATIONS)

	class Meta:
		model = Athlete
		fields = ('first_name', 'last_name', 'sport', 'recommendation')

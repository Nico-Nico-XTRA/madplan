from django.forms import ModelForm

from madplan.models import Dish

class DishForm(ModelForm):
	class Meta:
		model = Dish
		fields = ('name', 'description')
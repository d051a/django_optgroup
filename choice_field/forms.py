from django import forms
from choice_field.models import Categories, Stuff

class StuffModelForm(forms.ModelForm):

	class Meta:
		model = Stuff
		fields = ['name']

	def __init__(self, *args, **kwargs):
		super().__init__()
		categories_list = [
			[
				category, [[subcategory.id, subcategory] for subcategory in Categories.objects.filter(parent=category)
				if subcategory.parent == category]
			]
			for category in Categories.objects.all()
			if category.type == 1]
		self.fields['categories'] = forms.ChoiceField(choices=categories_list)

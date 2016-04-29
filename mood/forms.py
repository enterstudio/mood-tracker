from django.contrib.auth import get_user_model
from django import forms

from django.utils.translation import ugettext_lazy as _


from mood.models import Day, Entry, Attribute, Consumable, Dietary, Drink

from mood.choices import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class DrinkAddForm(forms.ModelForm):
    class Meta:
        model = Drink
        exclude = ['day','user']

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'attr_name form-control'}))
    track_daily = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'track_daily_field'}))
    calories = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'calories_field form-control'}))
    volume = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'volume_field form-control'}))




class EntryAddForm(forms.ModelForm):
	class Meta:
		model = Entry
		exclude = ['day','user']

	description = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add a Short Description (Optional)', 'rows':'3'}))

	tod = forms.ChoiceField(choices = TIME_OF_DAY_CHOICES, label = "Time of Day", required=True, widget=forms.Select(attrs={'class':'entry_field'}))

	happiness_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	motivation_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	anger_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	anxiety_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	energy_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))


class EntryUpdateForm(forms.ModelForm):
	class Meta:
		model = Entry
		exclude = ['day','user']

	description = forms.CharField(required=False, max_length=200, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add a Short Description (Optional)', 'rows':'3'}))

	tod = forms.ChoiceField(choices = TIME_OF_DAY_CHOICES, label = "Time of Day", required=True, widget=forms.Select(attrs={'class':'entry_field'}))

	happiness_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	motivation_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	anger_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	anxiety_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))
	energy_level = forms.IntegerField(widget=forms.TextInput(attrs={'class':'entry_field'}))

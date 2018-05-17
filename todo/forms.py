from django import forms

class todoForm(forms.Form):
	text = forms.CharField(max_length=30,
		widget=forms.TextInput(
			attrs = {'class' : 'form-control', 'placeholder' : 'Enter todo e.g. To edit my cv', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
		
from django import forms

class ReivewForm(forms.Form):
    # the variable create here will connect to TextInput widget of html 
    # with maybe defined a label
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your review here')
from django import forms
from .models import Review
from django.forms import ModelForm
# class ReivewForm(forms.Form):
#     # the variable create here will connect to TextInput widget of html 
#     # with maybe defined a label
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     # use widget in python and call css style using "attrs={'class':'myform'}"
#     # all the attribute of certain HTML tag can be passed in as a dictionary in the "attrs" of widget
#     review = forms.CharField(label='Please write your review here', widget=forms.Textarea(attrs={'class':'myform', 'rows': '2', 'cols': '2'}))

# Form interacte with model
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # pass all the model fields as form fields
        # fields = ['first_name', 'last_name', 'stars']
        # over write label
        labels = {
            'first_name': "YOUR FIRST NAME",
            'last_name' : "Last Name",
            'stars':'Rating'
        }
        error_messages = {
            'stars':{
                'min_value': "YO! Min value is 1",
                'max_value': "YO! YO! Max value is 5",
            }
        }
            
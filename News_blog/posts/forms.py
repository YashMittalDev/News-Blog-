'''
we can create forms in two ways either 
1. directly with the help of models we defined by inheriting ModelForm class which is in forms.
2. usinf Form class which is in forms module.

now 
2. 
from django import forms
now , create a class which inherits forms.Form
class PostCreationForm(forms.Form)
then create fields with the name you want or we can say the name within the models
    title = forms.CharField(max_length=225) and use Charfield , TextInput ,....some options like that

    when we create object of the class that means we have a form.

'''
from django import forms

class PostCreationForm(forms.Form):
    title = forms.CharField(max_length=225)
    description = forms.CharField()
    author = forms.CharField()

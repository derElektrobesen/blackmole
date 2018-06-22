from django import forms

class ImageForm(forms.Form):
    image = forms.FileField(label='Select an image', required=True)
    image_name = forms.CharField(min_length=1, max_length=150, required=True)

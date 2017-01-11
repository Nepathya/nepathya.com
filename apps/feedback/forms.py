from django import forms
from ..feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email','required': True}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message','required': True})
        }

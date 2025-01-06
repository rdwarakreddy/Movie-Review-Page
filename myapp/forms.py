from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MovieReview


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['movie_name', 'rating', 'review', 'photo', 'link']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'rows': 5}),
        }
    def __init__(self, *args, **kwargs):
        super(MovieReviewForm, self).__init__(*args, **kwargs)
        
        # Add CSS classes to form fields
        self.fields['movie_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
        self.fields['review'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control-file'})
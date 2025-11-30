from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import User

# Registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs= {'class':'forms-contol',
                                                                            'placeholder':'Email'}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, widget=forms.select(attrs={
        'class' : 'form-control'
    }))

    class Meta:
        model = User
        field = ('username', 'email', 'user_type', 'password1', 'password2') # simply the form fields my user will fill
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            })
        }
    
    # Passwords
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder': 'Confirm Password'})

# Login Form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'password',
    }))

# Profile form : update on account profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'bio', 'profile_image')
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' :forms.TextInput(attrs={'class' : 'form-control'}),
            'bio' :forms.Textarea(attrs={'class' : 'form-control', 'rows' :3})
        }
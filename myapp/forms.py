from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import StudentProfile
from .models import BookRequest

class StudentIDForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('student_id','Faculty','Batch','image2')

    student_id = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your student ID',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    Faculty = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your student ID',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    Batch= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your student ID',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    image2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class Signup(UserCreationForm):
   
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ('book',)

    def __init__(self, *args, **kwargs):
        super(BookRequestForm, self).__init__(*args, **kwargs)
        self.fields['book'].widget.attrs.update({'class': 'form-control'})

class BookApprovalForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ('approved',)
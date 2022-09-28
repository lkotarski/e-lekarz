from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, DateInput
from .models import CustomUser, DoctorProfile, Appointment, Comment

class NewForm(UserCreationForm):
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'second_name', 'last_name', 'email', 'PESEL', 'city', 'address', 'phone_number')

    def save(self, mode, commit=True):
        user = super(NewForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if mode=='doctor':
            user.isDoctor = True
        if commit:
            user.save()
        return user

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'second_name', 'last_name', 'email', 'PESEL', 'city', 'address', 'phone_number')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Hasła nie są identyczne.")
        return cd['password2']

class DoctorProfileForm(forms.ModelForm):
    PWZ_number = forms.IntegerField(required=True) # <- set her
    
    class Meta:
        model = DoctorProfile
        fields = ("description", "PWZ_number", "facility", "city", 'address', 'spec1', 'spec2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'second_name', 'email', 'phone_number', 'PESEL', 'city', 'address', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': Textarea()
        }

class AppointmentFormAnonymous(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'phone_number', 'date', 'hour', 'cause')

        widgets = {
                'date': DateInput(attrs={'type': 'date', 'placeholder':'Data wizyty'}),
        }

class AppointmentFormLogged(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('date', 'hour', 'cause')

        widgets = {
                'date': DateInput(attrs={'type': 'date', 'placeholder':'Data wizyty'}),
        }

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, AuthenticationForm

from .models import UserBase


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Email address',
            'id': 'login-username'
        }
    )
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    )
    )


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label='Enter Username',
        min_length=4,
        max_length=50,
        help_text='Required'
    )
    email = forms.EmailField(
        max_length=100,
        help_text='Required',
        error_messages={'required': 'Sorry, you will need an email'}
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Email',
            'id': 'form-email'
        }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        usr = UserBase.objects.filter(email=email)
        if not usr:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Account Email (can not be changed)',
                             max_length=200,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control mb-3',
                                        'placeholder': 'email',
                                        'id': 'form-email',
                                        'readonly': 'readonly'})
                             )

    user_name = forms.CharField(label='User Name',
                                max_length=255,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control mb-3',
                                           'placeholder': 'Username',
                                           'id': 'form-user_name',
                                           'readonly': 'readonly'})
                                )

    first_name = forms.CharField(label='Full Name',
                                 max_length=255,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control mb-3',
                                            'placeholder': 'Full Name',
                                            'id': 'form-fullname'})
                                 )

    phone_number = forms.CharField(label='Phone Number',
                                   max_length=12,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control mb-3',
                                              'placeholder': 'Phone Number',
                                              'id': 'form-phonenumber'})
                                   )
    Address = forms.CharField(label='Address',
                           max_length=255,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control mb-3',
                                      'placeholder': 'Address',
                                      'id': 'form-address'})
                           )

    city = forms.CharField(label='city',
                           max_length=255,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control mb-3',
                                      'placeholder': 'city',
                                      'id': 'form-city'})
                           )

    pincode = forms.CharField(label='pin',
                              max_length=255,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control mb-3',
                                         'placeholder': 'pin',
                                         'id': 'form-pin'})
                              )


    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name','phone_number','city','pincode','Address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

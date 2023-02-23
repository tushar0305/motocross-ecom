from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from orders.views import user_orders
from .forms import RegistrationForm, UserEditForm
from django.contrib.sites.shortcuts import get_current_site

from .models import UserBase
from .tokens import account_activation_token


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request,
                  'store/account/user/dashboard.html',
                  {'section': 'profile', 'orders': orders})
    # return render(request, 'store/account/user/dashboard.html')


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        """email = request.POST.get("email", '')
        city = request.POST.get("city", '')
        pincode = request.POST.get("pincode", '')
        address = request.POST.get("Address", '')
        # UserBase.objects.filter(email=email).update(city=city, pincode=pincode, Address=address)"""
        user_form.save()
        if user_form.is_valid():
            user_form.save()

    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'store/account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')

def delete(request):
    return render(request, 'store/account/user/delete.html')


def account_register(request):
    """if request.user.is_authenticated:
        return redirect('account:dashboard')"""

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.status = False
            user.save()
            current_site = get_current_site(request)
            new_token = account_activation_token.make_token(user)
            subject = 'Activate your Account'
            message = render_to_string('store/account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': new_token,
            })
            user.email_user(subject=subject, message=message)
            return render(request,'store/account/registration/account_successfull.html',{'form':registerForm})
    else:
        registerForm = RegistrationForm()
    return render(request, 'store/account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'store/account/registration/activation_invalid.html')

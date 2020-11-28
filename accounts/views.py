from .forms import SignUpForm
from django.shortcuts import get_object_or_404, render, redirect
from .utils import send_confirmation_email


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_valid = False
            user.save()
            send_confirmation_email(user)
            redirect(request, 'registration/signup_success.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
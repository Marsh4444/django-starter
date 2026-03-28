"""
apps/accounts/views.py

Auth views: register, login, logout, profile view, profile edit.
Uses Django's built-in LoginView and LogoutView where possible.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, ProfileUpdateForm
from .models import CustomUser


# ── Registration ──────────────────────────────────────────────────────────────

class RegisterView(CreateView):
    """
    Class-based view for user registration.
    On success, logs the user in automatically and redirects to dashboard.
    """
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f"Welcome, {user.get_full_name_or_username()}!")
        return redirect('accounts:dashboard')

    def dispatch(self, request, *args, **kwargs):
        # Redirect already logged-in users away from register page
        if request.user.is_authenticated:
            return redirect('accounts:dashboard')
        return super().dispatch(request, *args, **kwargs)


# ── Login ─────────────────────────────────────────────────────────────────────

class CustomLoginView(LoginView):
    """
    Extends Django's LoginView.
    Redirects authenticated users and adds a flash message on success.
    """
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f"Welcome back, {form.get_user().get_full_name_or_username()}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


# ── Logout ────────────────────────────────────────────────────────────────────

def logout_view(request):
    """Simple logout. POST preferred but GET accepted for convenience."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('accounts:login')


# ── Dashboard ─────────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    """
    Placeholder dashboard. Customize this per project.
    You can split into role-based dashboards here, e.g.:
        if request.user.role == 'admin':
            return render(request, 'accounts/dashboard_admin.html')
    """
    return render(request, 'accounts/dashboard.html', {
        'user': request.user,
    })


# ── Profile ───────────────────────────────────────────────────────────────────

@login_required
def profile_view(request):
    """View the current user's profile."""
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def profile_edit(request):
    """Edit the current user's profile."""
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {'form': form})

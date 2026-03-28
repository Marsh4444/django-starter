"""
apps/accounts/decorators.py

Role-based access control decorators.

Usage:
    from apps.accounts.decorators import role_required

    @login_required
    @role_required(['admin', 'staff'])
    def admin_only_view(request):
        ...
"""

from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def role_required(roles):
    """
    Decorator that restricts a view to users with one of the specified roles.

    Args:
        roles (list): List of role strings that are allowed, e.g. ['admin', 'staff']

    Behaviour:
        - If user is not logged in → redirect to login
        - If user's role is not in the allowed list → redirect to dashboard with error message
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')

            if request.user.role not in roles:
                messages.error(request, "You do not have permission to access that page.")
                return redirect('accounts:dashboard')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

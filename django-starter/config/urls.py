"""
config/urls.py — Root URL configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts (login, logout, register, profile)
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),

    # Your app routes go here, e.g.:
    # path('', include('apps.core.urls', namespace='core')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

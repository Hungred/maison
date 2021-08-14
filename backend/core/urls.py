"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from utils import error_handlers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('schedule:index'), name='root'),
    path('login/', include('apps.login.urls')),
    path('schedule/', include('apps.schedule.urls')),
    path('reservation/', include('apps.reservation.urls')),
    path('order/', include('apps.order.urls')),
    path('report/', include('apps.report.urls')),
    path('feedback/', include('apps.feedback.urls')),
    path('customer/', include('apps.customer.urls')),
    path('event/', include('apps.event.urls')),
    path('admin/', admin.site.urls),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'utils.error_handlers.permission_denied'

"""CTF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import re_path as url

from django.contrib import admin
import app.views as views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from django.views.generic import TemplateView

handler404 = "app.views.handler404"
handler500 = "app.views.handler500"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    url(r"^$", views.index),
    url(r"^login/", views.teamlogin),
    url(r"^register/", views.register),
    url(r"^quest/", views.quest),
    url(r"^logout/", views.teamlogout),
    url(r"^leaderboard/", views.leaderboard),
    url(r"^timer/", views.timer),
    url(r"^hint/", views.hint),
    path("user/<str:username>",views.profile),
    url(r"^uservalidator/", views.validate_username),
    url(r"^instructions/", views.instructions),
    url(r"^about/", views.about),
    url(r"^waiting/",views.waiting),
    url(r"^wait-time/",views.waiting_time),
    # url(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # # path('password-reset/', views.custom_password_reset, name='password_reset'),
    # url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # # url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # url(r'^password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path("machine/<int:id>", views.machine),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

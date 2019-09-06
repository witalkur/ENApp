"""ENapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from mainApp import views as today_views
from mainApp.views import (BendTestUpdateView, DelaminationTestUpdateView, ShearTestUpdateView, BendTestDeleteView, 
DelaminationTestDeleteView, ShearTestDeleteView, NonconformityUpdateView, NonconformityDeleteView, NonconformitiesView,
NonconformityDetailView, NonconformityCreateView, PersonsView, PersonUpdateView, PersonDeleteView, PersonCreateView,
PersonDetailView, ToolsView, ToolUpdateView, ToolDeleteView, ToolCreateView, ToolDetailView, bendtestfilterView,
Wood_types_UpdateView, Wood_types_DeleteView, Strength_class_UpdateView, Strength_class_DeleteView)
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', today_views.today, name='today'),
    path('bendtest/', today_views.bendtest, name='bendtest'),
    path('testdelamination/', today_views.TestDelaminationView, name='testdelamination'),
    path('testshear/', today_views.TestShearView, name='testshear'),
    path('datetests/', today_views.DateTestsView, name='date_tests'),
    path('bendtest/<int:pk>/update/',  BendTestUpdateView.as_view(), name='bend-test-update'),
    path('delaminationtest/<int:pk>/update/',  DelaminationTestUpdateView.as_view(), name='delamination-test-update'),
    path('sheartest/<int:pk>/update/',  ShearTestUpdateView.as_view(), name='shear-test-update'),
    path('bendtest/<int:pk>/delete/', BendTestDeleteView.as_view(), name='bend-test-delete'),
    path('delaminationtest/<int:pk>/delete/', DelaminationTestDeleteView.as_view(), name='delamination-test-delete'),
    path('sheartest/<int:pk>/delete/', ShearTestDeleteView.as_view(), name='shear-test-delete'),
    path('nonconformities/', today_views.NonconformitiesView, name='nonconformities'),
    path('nonconformity/<int:pk>/update/',  NonconformityUpdateView.as_view(), name='nonconformity-update'),
    path('nonconformity/<int:pk>/delete/', NonconformityDeleteView.as_view(), name='nonconformity-delete'),
    path('nonconformity/detail/<int:pk>', NonconformityDetailView.as_view(), name='nonconformity'),
    path('nonconformity/create', today_views.NonconformityCreateView, name='nonconformity-create'),
    path('persons/', today_views.PersonsView, name='persons'),
    path('person/<int:pk>/update/', PersonUpdateView.as_view(), name='person-update'),
    path('person/<int:pk>/delete/', PersonDeleteView.as_view(), name='person-delete'),
    path('person/detail/<int:pk>', PersonDetailView.as_view(), name='person'),
    path('person/create', today_views.PersonCreateView, name='person-create'),
    path('tools/', today_views.ToolsView, name='tools'),
    path('tool/<int:pk>/update/', ToolUpdateView.as_view(), name='tool-update'),
    path('tool/<int:pk>/delete/', ToolDeleteView.as_view(), name='tool-delete'),
    path('tool/detail/<int:pk>', ToolDetailView.as_view(), name='tool'),
    path('tool/create', today_views.ToolCreateView, name='tool-create'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('bendtestfilter/', today_views.bendtestfilterView, name='bendtestfilter'),
    path('delamtestfilter/', today_views.DelaminationTestfilterView, name='delamtestfilter'),
    path('sheartestfilter/', today_views.ShearTestfilterView, name='sheartestfilter'),
    path('settings/', today_views.SettingsView, name='settings'),
    path('woodtype/<int:pk>/update/', Wood_types_UpdateView.as_view(), name='woodtype-update'),
    path('woodtype/<int:pk>/delete/', Wood_types_DeleteView.as_view(), name='woodtype-delete'),
    path('strengthclass/<int:pk>/update/', Strength_class_UpdateView.as_view(), name='strengthclass-update'),
    path('strengthclass/<int:pk>/delete/', Strength_class_DeleteView.as_view(), name='strengthclass-delete'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    name='password_reset_confirm'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
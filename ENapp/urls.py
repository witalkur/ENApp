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
NonconformityDetailView, NonconformityCreateView)

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
    path('nonconformity/create', NonconformityCreateView, name='nonconformity-create'),
]

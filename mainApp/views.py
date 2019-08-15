from django.shortcuts import render, redirect
from .forms import BendtestForm, TestDelaminationForm, TestShearForm, DateForm, NonconformityForm
from django.contrib import messages
from .models import TestLamella, TestDelamination, TestShear, Nonconformity
import datetime
from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView

def today(request):
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			today_date = form.cleaned_data.get('need_date')
			return redirect('date_tests')
	else:
		form = DateForm()
		today_date = datetime.date.today()
	bendtests = TestLamella.objects.filter(test_date=today_date).order_by('test_number')
	delamination_tests = TestDelamination.objects.filter(test_date=today_date).order_by('test_number')
	shear_tests = TestShear.objects.filter(test_date=today_date).order_by('test_number')
	return render(request, 'mainApp/today.html', {'bendtests': bendtests, 'delaminationtests': delamination_tests, 
		'sheartests': shear_tests, 'date': today_date, 'date_form': DateForm,})

def bendtest(request):
	if request.method == 'POST':
		form = BendtestForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Новый тест на изгиб сохранен!')
			return redirect('today')
	else:
		form = BendtestForm()
	return render(request, 'mainApp/bendtest.html', {'form': form})

def TestDelaminationView(request):
	if request.method == 'POST':
		form = TestDelaminationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Новый тест на деламинацию сохранен!')
			return redirect('today')
	else:
		form = TestDelaminationForm()
	return render(request, 'mainApp/TestDelamination.html', {'form': form})

def TestShearView(request):
	if request.method == 'POST':
		form = TestShearForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Новый тест на срез сохранен!')
			return redirect('today')
	else:
		form = TestShearForm()
	return render(request, 'mainApp/TestShear.html', {'form': form})

def DateTestsView(request):
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			today_date = form.cleaned_data.get('need_date')
			bendtests = TestLamella.objects.filter(test_date=today_date).order_by('test_number')
			delamination_tests = TestDelamination.objects.filter(test_date=today_date).order_by('test_number')
			shear_tests = TestShear.objects.filter(test_date=today_date).order_by('test_number')
			return render(request, 'mainApp/today.html', {'bendtests': bendtests, 'delaminationtests': delamination_tests, 
				'sheartests': shear_tests, 'date': today_date, 'date_form': DateForm})

class BendTestUpdateView(UpdateView):
	model = TestLamella
	success_url = '/'
	template_name = 'mainApp/TestUpdate.html'
	fields = ['test_date', 'test_number', 'equipment', 'type_of_wood', 'strength_class', 'glue',
		'lamellas_thickness', 'lamellas_width', 'lamellas_length', 'fj_length', 'fj_path', 'fj_gap',
		'fj_angle', 'fj_orientation', 'lamellas_left_moisture', 'lamellas_right_moisture', 'glue_pressure',
		'pressure_time', 'glue_use_amount', 'glue_batch_number', 'glue_expiration_date', 'lamellas_param',
		'lamellas_took_person', 'force_crash', 'lamellas_strength', 'by_fj_crash', 'base_fj_crash',
		'out_of_fj_crash', 'comment',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на изгиб был изменен!')
		return super().post(request, *args, **kwargs)

class DelaminationTestUpdateView(UpdateView):
	model = TestDelamination
	success_url = '/'
	template_name = 'mainApp/TestUpdate.html'
	fields = ['test_date', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_temperature',
		'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'layer_out_percent', 'comment',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на деламинацию был изменен!')
		return super().post(request, *args, **kwargs)

class ShearTestUpdateView(UpdateView):
	model = TestShear
	success_url = '/'
	template_name = 'mainApp/TestUpdate.html'
	fields = ['test_date', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_temperature',
		'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'layer_ripped_percent1', 'layer_ripped_percent2',
		 'layer_ripped_percent3', 'layer_ripped_percent4', 'layer_ripped_percent5', 'layer_ripped_percent_average',
		 'force_crash', 'comment',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на срез был изменен!')
		return super().post(request, *args, **kwargs)

class BendTestDeleteView(DeleteView):
	model = TestLamella
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

class DelaminationTestDeleteView(DeleteView):
	model = TestDelamination
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

class ShearTestDeleteView(DeleteView):
	model = TestShear
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

def NonconformitiesView(request):
	nonconformities = Nonconformity.objects.all().order_by('nonconformity_date')
	return render(request, 'mainApp/nonconformities.html', {'nonconformities': nonconformities,})


class NonconformityUpdateView(UpdateView):
	model = Nonconformity
	success_url = '/nonconformities'
	template_name = 'mainApp/nonconformity_update.html'
	fields = ['name', 'description', 'resp_person', 'nonconformity_date',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Несоответствие отредактировано!')
		return super().post(request, *args, **kwargs)

class NonconformityDeleteView(DeleteView):
	model = Nonconformity
	success_url = '/nonconformities'
	template_name = 'mainApp/nonconformity_confirm_delete.html'

class NonconformityDetailView(DetailView):
	model = Nonconformity

def NonconformityCreateView(request):
	if request.method == 'POST':
		form = NonconformityForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Новое несоответствие добавлено!')
			return redirect('nonconformities')
	else:
		form = NonconformityForm()
	return render(request, 'mainApp/nonconformity_form.html', {'form': form,})
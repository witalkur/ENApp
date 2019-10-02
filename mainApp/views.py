from django.shortcuts import render, redirect, get_object_or_404
from .forms import (BendtestForm, TestDelaminationForm, TestShearForm, DateForm, NonconformityForm, 
	PersonForm, ToolForm, BendtestFilterForm, DelaminationTestFilterForm, ShearTestFilterForm, Wood_typeForm, strength_class_typesForm)
from django.contrib import messages
from .models import TestLamella, TestDelamination, TestShear, Nonconformity, Person, Tool, Wood_types, strength_class_types
import datetime
from django.views.generic import UpdateView, DeleteView, ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def today(request):
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			today_date = form.cleaned_data.get('need_date')
			return redirect('date_tests')
	else:
		form = DateForm()
		today_date = datetime.date.today()
		user = get_object_or_404(User, username=request.user.username)
	bendtests = TestLamella.objects.filter(test_date=today_date, author=user).order_by('test_number')
	delamination_tests = TestDelamination.objects.filter(test_date=today_date, author=user).order_by('test_number')
	shear_tests = TestShear.objects.filter(test_date=today_date, author=user).order_by('test_number')
	return render(request, 'mainApp/today.html', {'bendtests': bendtests, 'delaminationtests': delamination_tests, 
		'sheartests': shear_tests, 'date': today_date, 'date_form': DateForm,})

@login_required
def bendtest(request):
	if request.method == 'POST':
		form = BendtestForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, f'Новый тест на изгиб сохранен!')
			return redirect('today')
	else:
		form = BendtestForm()
	return render(request, 'mainApp/bendtest.html', {'form': form})


class BendTestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = TestLamella

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False


class TestShearDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = TestShear

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False


class DelamTestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = TestDelamination

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False


@login_required
def TestDelaminationView(request):
	if request.method == 'POST':
		form = TestDelaminationForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, f'Новый тест на деламинацию сохранен!')
			return redirect('today')
	else:
		form = TestDelaminationForm()
	return render(request, 'mainApp/TestDelamination.html', {'form': form})

@login_required
def TestShearView(request):
	if request.method == 'POST':
		form = TestShearForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, f'Новый тест на срез сохранен!')
			return redirect('today')
	else:
		form = TestShearForm()
	return render(request, 'mainApp/TestShear.html', {'form': form})

@login_required
def DateTestsView(request):
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			user = get_object_or_404(User, username=request.user.username)
			today_date = form.cleaned_data.get('need_date')
			bendtests = TestLamella.objects.filter(test_date=today_date, author=user).order_by('test_number')
			delamination_tests = TestDelamination.objects.filter(test_date=today_date, author=user).order_by('test_number')
			shear_tests = TestShear.objects.filter(test_date=today_date, author=user).order_by('test_number')
			return render(request, 'mainApp/today.html', {'bendtests': bendtests, 'delaminationtests': delamination_tests, 
				'sheartests': shear_tests, 'date': today_date, 'date_form': DateForm})


class BendTestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = TestLamella
	success_url = '/bendtest/{id}/detail/'
	form_class = BendtestForm
	template_name = 'mainApp/BendTestUpdate.html'
	'''fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'strength_class', 'glue', 
		'glue_harderner_amount', 'lamellas_thickness', 'lamellas_width', 'lamellas_length', 'fj_length', 'fj_path', 'fj_gap',
		'fj_angle', 'fj_orientation', 'lamellas_left_moisture', 'lamellas_right_moisture', 'glue_pressure',
		'pressure_time', 'glue_use_amount', 'glue_batch_number', 'glue_expiration_date', 'lamellas_param',
		'lamellas_took_person', 'force_crash', 'time_of_testing', 'lamellas_strength', 'passed', 'by_fj_crash', 'base_fj_crash',
		'out_of_fj_crash', 'comment', 'photo']'''

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на изгиб был изменен!')
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False

class DelaminationTestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = TestDelamination
	success_url = '/delaminationtest/{id}/detail/'
	form_class = TestDelaminationForm
	template_name = 'mainApp/DelamTestUpdate.html'
	'''fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_harderner_amount', 
		'glue_temperature', 'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'layer_out_percent', 'passed', 'comment', 'photo',]'''

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на деламинацию был изменен!')
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False


class ShearTestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = TestShear
	success_url = '/sheartest/{id}/detail/'
	template_name = 'mainApp/ShearTestUpdate.html'
	form_class = TestShearForm
	'''fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_temperature',
		'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_harderner_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'time_of_testing', 'layer_ripped_percent1', 'layer_ripped_percent2',
		 'layer_ripped_percent3', 'layer_ripped_percent4', 'layer_ripped_percent5', 'layer_ripped_percent_average',
		 'force_crash', 'passed', 'comment', 'photo']'''

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на срез был изменен!')
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False

class BendTestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = TestLamella
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False

class DelaminationTestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = TestDelamination
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

class ShearTestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = TestShear
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

@login_required
def NonconformitiesView(request):
	user = get_object_or_404(User, username=request.user.username)
	nonconformities = Nonconformity.objects.filter(author=user).order_by('nonconformity_date')
	return render(request, 'mainApp/nonconformities.html', {'nonconformities': nonconformities,})


class NonconformityDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Nonconformity

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False



class NonconformityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Nonconformity
	success_url = '/nonconformities'
	template_name = 'mainApp/nonconformity_update.html'
	form_class = NonconformityForm
	#fields = ['name', 'description', 'resp_person', 'nonconformity_date',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Несоответствие отредактировано!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		nonconformity = self.get_object()
		if self.request.user == nonconformity.author:
			return True
		return False

class NonconformityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Nonconformity
	success_url = '/nonconformities'
	template_name = 'mainApp/nonconformity_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Несоответствие удалено!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		nonconformity = self.get_object()
		if self.request.user == nonconformity.author:
			return True
		return False



@login_required
def NonconformityCreateView(request):
	if request.method == 'POST':
		form = NonconformityForm(request.POST)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, f'Новое несоответствие добавлено!')
			return redirect('nonconformities')
	else:
		form = NonconformityForm()
	return render(request, 'mainApp/nonconformity_form.html', {'form': form,})

@login_required
def PersonsView(request):
	user = get_object_or_404(User, username=request.user.username)
	persons = Person.objects.filter(author=user).order_by('name')
	return render(request, 'mainApp/persons.html', {'persons': persons,})

class PersonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Person
	success_url = '/persons'
	template_name = 'mainApp/person_update.html'
	form_class = PersonForm
	#fields = ['name', 'position', 'training_date', 'next_training_date', 'comment',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Данные о сотруднике сохранены!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		person = self.get_object()
		if self.request.user == person.author:
			return True
		return False

class PersonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Person
	success_url = '/persons'
	template_name = 'mainApp/person_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Данные о сотруднике удалены!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		person = self.get_object()
		if self.request.user == person.author:
			return True
		return False

@login_required
def PersonCreateView(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, f'Данные о новом сотруднике добавлены!')
			return redirect('persons')
	else:
		form = PersonForm()
	return render(request, 'mainApp/person_form.html', {'form': form,})

class PersonDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Person

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False

@login_required
def ToolsView(request):
	user = get_object_or_404(User, username=request.user.username)
	tools = Tool.objects.filter(author=user).order_by('name')
	return render(request, 'mainApp/tools.html', {'tools': tools,})

class ToolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Tool
	success_url = '/tools'
	template_name = 'mainApp/tool_update.html'
	form_class = ToolForm
	#fields = ['name', 'description', 'resp_person', 'calibration_date', 'next_calibration_date',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Информация сохранена!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		tool = self.get_object()
		if self.request.user == tool.author:
			return True
		return False


class ToolDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Tool
	success_url = '/tools'
	template_name = 'mainApp/tool_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Данные удалены!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		tool = self.get_object()
		if self.request.user == tool.author:
			return True
		return False

def ToolCreateView(request):
	if request.method == 'POST':
		form = ToolForm(request.POST)
		if form.is_valid():
			form.instance.author = request.user
			form.save()
			messages.success(request, f'Данные добавлены!')
			return redirect('tools')
	else:
		form = ToolForm()
	return render(request, 'mainApp/tool_form.html', {'form': form,})

class ToolDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Tool

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False


@login_required
def bendtestfilterView(request):
	user = get_object_or_404(User, username=request.user.username)
	bendtests = TestLamella.objects.filter(author=user).order_by('test_number')
	if request.method == 'POST':
		form = BendtestFilterForm(request.POST)
		if form.is_valid():
			if form.cleaned_data.get('start_test_date'):
				start_test_date = form.cleaned_data.get('start_test_date')
				bendtests = bendtests.filter(test_date__gte=start_test_date).order_by('test_number')
			if form.cleaned_data.get('end_test_date'):
				end_test_date = form.cleaned_data.get('end_test_date')
				bendtests = bendtests.filter(test_date__lte=end_test_date).order_by('test_number')
			if form.cleaned_data.get('type_of_wood'):
				type_of_wood = form.cleaned_data.get('type_of_wood')
				bendtests = bendtests.filter(type_of_wood=type_of_wood).order_by('test_number')
			if form.cleaned_data.get('start_test_time'):
				start_test_time = form.cleaned_data.get('start_test_time')
				bendtests = bendtests.filter(test_time__gte=start_test_time).order_by('test_number')
			if form.cleaned_data.get('end_test_time'):
				end_test_time = form.cleaned_data.get('end_test_time')
				bendtests = bendtests.filter(test_time__lte=end_test_time).order_by('test_number')
			if form.cleaned_data.get('test_number'):
				test_number = form.cleaned_data.get('test_number')
				bendtests = bendtests.filter(test_number=test_number).order_by('test_number')
			if form.cleaned_data.get('equipment'):
				equipment = form.cleaned_data.get('equipment')
				bendtests = bendtests.filter(equipment__iexact=equipment).order_by('test_number')	
			if form.cleaned_data.get('strength_class'):
				strength_class = form.cleaned_data.get('strength_class')
				bendtests = bendtests.filter(strength_class=strength_class).order_by('test_number')	
			if form.cleaned_data.get('glue'):
				glue = form.cleaned_data.get('glue')
				bendtests = bendtests.filter(glue__iexact=glue).order_by('test_number')
			if form.cleaned_data.get('glue_harderner_amount'):
				glue_harderner_amount = form.cleaned_data.get('glue_harderner_amount')
				bendtests = bendtests.filter(glue_harderner_amount__iexact=glue_harderner_amount).order_by('test_number')
			if form.cleaned_data.get('lamellas_thickness_from'):
				lamellas_thickness_from = form.cleaned_data.get('lamellas_thickness_from')
				bendtests = bendtests.filter(lamellas_thickness__gte=lamellas_thickness_from).order_by('test_number')
			if form.cleaned_data.get('lamellas_thickness_to'):
				lamellas_thickness_to = form.cleaned_data.get('lamellas_thickness_to')
				bendtests = bendtests.filter(lamellas_thickness__lte=lamellas_thickness_to).order_by('test_number')
			if form.cleaned_data.get('fj_length'):
				fj_length = form.cleaned_data.get('fj_length')
				bendtests = bendtests.filter(fj_length=fj_length).order_by('test_number')
			if form.cleaned_data.get('fj_path'):
				fj_path = form.cleaned_data.get('fj_path')
				bendtests = bendtests.filter(fj_path=fj_path).order_by('test_number')
			if form.cleaned_data.get('fj_gap'):
				fj_gap = form.cleaned_data.get('fj_gap')
				bendtests = bendtests.filter(fj_gap=fj_gap).order_by('test_number')
			if form.cleaned_data.get('fj_angle'):
				fj_angle = form.cleaned_data.get('fj_angle')
				bendtests = bendtests.filter(fj_angle=fj_angle).order_by('test_number')
			if form.cleaned_data.get('fj_orientation'):
				fj_orientation = form.cleaned_data.get('fj_orientation')
				bendtests = bendtests.filter(fj_orientation=fj_orientation).order_by('test_number')
			if form.cleaned_data.get('lamellas_left_moisture_from'):
				lamellas_left_moisture_from = form.cleaned_data.get('lamellas_left_moisture_from')
				bendtests = bendtests.filter(lamellas_left_moisture__gte=lamellas_left_moisture_from).order_by('test_number')
			if form.cleaned_data.get('lamellas_left_moisture_to'):
				lamellas_left_moisture_to = form.cleaned_data.get('lamellas_left_moisture_to')
				bendtests = bendtests.filter(lamellas_left_moisture__lte=lamellas_left_moisture_to).order_by('test_number')
			if form.cleaned_data.get('lamellas_right_moisture_from'):
				lamellas_right_moisture_from = form.cleaned_data.get('lamellas_right_moisture_from')
				bendtests = bendtests.filter(lamellas_right_moisture__gte=lamellas_right_moisture_from).order_by('test_number')
			if form.cleaned_data.get('lamellas_right_moisture_to'):
				lamellas_right_moisture_to = form.cleaned_data.get('lamellas_right_moisture_to')
				bendtests = bendtests.filter(lamellas_right_moisture__lte=lamellas_right_moisture_to).order_by('test_number')
			if form.cleaned_data.get('glue_pressure_from'):
				glue_pressure_from = form.cleaned_data.get('glue_pressure_from')
				bendtests = bendtests.filter(glue_pressure__gte=glue_pressure_from).order_by('test_number')
			if form.cleaned_data.get('glue_pressure_to'):
				glue_pressure_to = form.cleaned_data.get('glue_pressure_to')
				bendtests = bendtests.filter(glue_pressure__lte=glue_pressure_to).order_by('test_number')
			if form.cleaned_data.get('pressure_time_from'):
				pressure_time_from = form.cleaned_data.get('pressure_time_from')
				bendtests = bendtests.filter(pressure_time__gte=pressure_time_from).order_by('test_number')
			if form.cleaned_data.get('pressure_time_to'):
				pressure_time_to = form.cleaned_data.get('pressure_time_to')
				bendtests = bendtests.filter(pressure_time__lte=pressure_time_to).order_by('test_number')
			if form.cleaned_data.get('glue_use_amount_from'):
				glue_use_amount_from = form.cleaned_data.get('glue_use_amount_from')
				bendtests = bendtests.filter(glue_use_amount__gte=glue_use_amount_from).order_by('test_number')
			if form.cleaned_data.get('glue_use_amount_to'):
				glue_use_amount_to = form.cleaned_data.get('glue_use_amount_to')
				bendtests = bendtests.filter(glue_use_amount__lte=glue_use_amount_to).order_by('test_number')
			if form.cleaned_data.get('glue_batch_number'):
				glue_batch_number = form.cleaned_data.get('glue_batch_number')
				bendtests = bendtests.filter(glue_batch_number=glue_batch_number).order_by('test_number')
			if form.cleaned_data.get('start_glue_expiration_date'):
				start_glue_expiration_date = form.cleaned_data.get('start_glue_expiration_date')
				bendtests = bendtests.filter(glue_expiration_date__gte=start_glue_expiration_date).order_by('test_number')
			if form.cleaned_data.get('end_glue_expiration_date'):
				end_glue_expiration_date = form.cleaned_data.get('end_glue_expiration_date')
				bendtests = bendtests.filter(glue_expiration_date__lte=end_glue_expiration_date).order_by('test_number')
			if form.cleaned_data.get('lamellas_param'):
				lamellas_param = form.cleaned_data.get('lamellas_param')
				bendtests = bendtests.filter(lamellas_param__iexact=lamellas_param).order_by('test_number')
			if form.cleaned_data.get('lamellas_took_person'):
				lamellas_took_person = form.cleaned_data.get('lamellas_took_person')
				bendtests = bendtests.filter(lamellas_took_person=lamellas_took_person).order_by('test_number')
			if form.cleaned_data.get('force_crash_from'):
				force_crash_from = form.cleaned_data.get('force_crash_from')
				bendtests = bendtests.filter(force_crash__gte=force_crash_from).order_by('test_number')
			if form.cleaned_data.get('force_crash_to'):
				force_crash_to = form.cleaned_data.get('force_crash_to')
				bendtests = bendtests.filter(force_crash__lte=force_crash_to).order_by('test_number')
			if form.cleaned_data.get('time_of_testing_from'):
				time_of_testing_from = form.cleaned_data.get('time_of_testing_from')
				bendtests = bendtests.filter(time_of_testing__gte=time_of_testing_from).order_by('test_number')
			if form.cleaned_data.get('time_of_testing_to'):
				time_of_testing_to = form.cleaned_data.get('time_of_testing_to')
				bendtests = bendtests.filter(time_of_testing__lte=time_of_testing_to).order_by('test_number')
			if form.cleaned_data.get('lamellas_strength_from'):
				lamellas_strength_from = form.cleaned_data.get('lamellas_strength_from')
				bendtests = bendtests.filter(lamellas_strength__gte=lamellas_strength_from).order_by('test_number')
			if form.cleaned_data.get('lamellas_strength_to'):
				lamellas_strength_to = form.cleaned_data.get('lamellas_strength_to')
				bendtests = bendtests.filter(lamellas_strength__lte=lamellas_strength_to).order_by('test_number')
			if form.cleaned_data.get('by_fj_crash_from'):
				by_fj_crash_from = form.cleaned_data.get('by_fj_crash_from')
				bendtests = bendtests.filter(by_fj_crash__gte=by_fj_crash_from).order_by('test_number')
			if form.cleaned_data.get('by_fj_crash_to'):
				by_fj_crash_to = form.cleaned_data.get('by_fj_crash_to')
				bendtests = bendtests.filter(by_fj_crash__lte=by_fj_crash_to).order_by('test_number')
			if form.cleaned_data.get('out_of_fj_crash_from'):
				out_of_fj_crash_from = form.cleaned_data.get('out_of_fj_crash_from')
				bendtests = bendtests.filter(out_of_fj_crash__gte=out_of_fj_crash_from).order_by('test_number')
			if form.cleaned_data.get('out_of_fj_crash_to'):
				out_of_fj_crash_to = form.cleaned_data.get('out_of_fj_crash_to')
				bendtests = bendtests.filter(out_of_fj_crash__lte=out_of_fj_crash_to).order_by('test_number')
			if form.cleaned_data.get('base_fj_crash_from'):
				base_fj_crash_from = form.cleaned_data.get('base_fj_crash_from')
				bendtests = bendtests.filter(base_fj_crash__gte=base_fj_crash_from).order_by('test_number')
			if form.cleaned_data.get('base_fj_crash_to'):
				base_fj_crash_to = form.cleaned_data.get('base_fj_crash_to')
				bendtests = bendtests.filter(base_fj_crash__lte=base_fj_crash_to).order_by('test_number')
			if form.cleaned_data.get('base_fj_crash_to'):
				base_fj_crash_to = form.cleaned_data.get('base_fj_crash_to')
				bendtests = bendtests.filter(base_fj_crash__lte=base_fj_crash_to).order_by('test_number')
			if form.cleaned_data.get('passed_true'):
				bendtests = bendtests.filter(passed=True).order_by('test_number')
			if form.cleaned_data.get('passed_false'):
				bendtests = bendtests.filter(passed=False).order_by('test_number')
			if form.cleaned_data.get('comment'):
				comment = form.cleaned_data.get('comment')
				bendtests = bendtests.filter(comment__icontains=comment).order_by('test_number')

	else:
		form = BendtestFilterForm()
	return render(request, 'mainApp/bendtestfilter.html', {'bendtests': bendtests, 'form': form, })


@login_required
def DelaminationTestfilterView(request):
	user = get_object_or_404(User, username=request.user.username)
	delamination_tests = TestDelamination.objects.filter(author=user).order_by('test_number')
	if request.method == 'POST':
		form = DelaminationTestFilterForm(request.POST)
		if form.is_valid():
			if form.cleaned_data.get('start_test_date'):
				start_test_date = form.cleaned_data.get('start_test_date')
				delamination_tests = delamination_tests.filter(test_date__gte=start_test_date).order_by('test_number')
			if form.cleaned_data.get('end_test_date'):
				end_test_date = form.cleaned_data.get('end_test_date')
				delamination_tests = delamination_tests.filter(test_date__lte=end_test_date).order_by('test_number')
			if form.cleaned_data.get('test_number'):
				test_number = form.cleaned_data.get('test_number')
				delamination_tests = delamination_tests.filter(test_number=test_number).order_by('test_number')
			if form.cleaned_data.get('equipment'):
				equipment = form.cleaned_data.get('equipment')
				delamination_tests = delamination_tests.filter(equipment__iexact=equipment).order_by('test_number')
			if form.cleaned_data.get('type_of_wood'):
				type_of_wood = form.cleaned_data.get('type_of_wood')
				delamination_tests = delamination_tests.filter(type_of_wood=type_of_wood).order_by('test_number')
			if form.cleaned_data.get('timber_params'):
				timber_params = form.cleaned_data.get('timber_params')
				delamination_tests = delamination_tests.filter(timber_params__iexact=timber_params).order_by('test_number')
			if form.cleaned_data.get('sorter_person'):
				sorter_person = form.cleaned_data.get('sorter_person')
				delamination_tests = delamination_tests.filter(sorter_person=sorter_person).order_by('test_number')
			if form.cleaned_data.get('fj_person'):
				fj_person = form.cleaned_data.get('fj_person')
				delamination_tests = delamination_tests.filter(fj_person=fj_person).order_by('test_number')
			if form.cleaned_data.get('glue_person'):
				glue_person = form.cleaned_data.get('glue_person')
				delamination_tests = delamination_tests.filter(glue_person=glue_person).order_by('test_number')
			if form.cleaned_data.get('marking_person'):
				marking_person = form.cleaned_data.get('marking_person')
				delamination_tests = delamination_tests.filter(marking_person=marking_person).order_by('test_number')
			if form.cleaned_data.get('air_moisture_from'):
				air_moisture_from = form.cleaned_data.get('air_moisture_from')
				delamination_tests = delamination_tests.filter(air_moisture__gte=air_moisture_from).order_by('test_number')
			if form.cleaned_data.get('air_moisture_to'):
				air_moisture_to = form.cleaned_data.get('air_moisture_to')
				delamination_tests = delamination_tests.filter(air_moisture__lte=air_moisture_to).order_by('test_number')
			if form.cleaned_data.get('wood_moisture_from'):
				wood_moisture_from = form.cleaned_data.get('wood_moisture_from')
				delamination_tests = delamination_tests.filter(wood_moisture__gte=wood_moisture_from).order_by('test_number')
			if form.cleaned_data.get('wood_moisture_to'):
				wood_moisture_to = form.cleaned_data.get('wood_moisture_to')
				delamination_tests = delamination_tests.filter(wood_moisture__lte=wood_moisture_to).order_by('test_number')
			if form.cleaned_data.get('glue_harderner_amount'):
				glue_harderner_amount = form.cleaned_data.get('glue_harderner_amount')
				delamination_tests = delamination_tests.filter(glue_harderner_amount__iexact=glue_harderner_amount).order_by('test_number')
			if form.cleaned_data.get('air_temperature_from'):
				air_temperature_from = form.cleaned_data.get('air_temperature_from')
				delamination_tests = delamination_tests.filter(air_temperature__gte=air_temperature_from).order_by('test_number')
			if form.cleaned_data.get('air_temperature_to'):
				air_temperature_to = form.cleaned_data.get('air_temperature_to')
				delamination_tests = delamination_tests.filter(air_temperature__lte=air_temperature_to).order_by('test_number')
			if form.cleaned_data.get('wood_temperature_from'):
				wood_temperature_from = form.cleaned_data.get('wood_temperature_from')
				delamination_tests = delamination_tests.filter(wood_temperature__gte=wood_temperature_from).order_by('test_number')
			if form.cleaned_data.get('wood_temperature_to'):
				wood_temperature_to = form.cleaned_data.get('wood_temperature_to')
				delamination_tests = delamination_tests.filter(wood_temperature__lte=wood_temperature_to).order_by('test_number')
			if form.cleaned_data.get('glue'):
				glue = form.cleaned_data.get('glue')
				delamination_tests = delamination_tests.filter(glue__iexact=glue).order_by('test_number')
			if form.cleaned_data.get('glue_batch_number'):
				glue_batch_number = form.cleaned_data.get('glue_batch_number')
				delamination_tests = delamination_tests.filter(glue_batch_number=glue_batch_number).order_by('test_number')
			if form.cleaned_data.get('start_glue_expiration_date'):
				start_glue_expiration_date = form.cleaned_data.get('start_glue_expiration_date')
				delamination_tests = delamination_tests.filter(glue_expiration_date__gte=start_glue_expiration_date).order_by('test_number')
			if form.cleaned_data.get('end_glue_expiration_date'):
				end_glue_expiration_date = form.cleaned_data.get('end_glue_expiration_date')
				delamination_tests = delamination_tests.filter(glue_expiration_date__lte=end_glue_expiration_date).order_by('test_number')
			if form.cleaned_data.get('sample_thickness_from'):
				sample_thickness_from = form.cleaned_data.get('sample_thickness_from')
				delamination_tests = delamination_tests.filter(sample_thickness__gte=sample_thickness_from).order_by('test_number')
			if form.cleaned_data.get('sample_thickness_to'):
				sample_thickness_to = form.cleaned_data.get('sample_thickness_to')
				delamination_tests = delamination_tests.filter(sample_thickness__lte=sample_thickness_to).order_by('test_number')
			if form.cleaned_data.get('sample_width_from'):
				sample_width_from = form.cleaned_data.get('sample_width_from')
				delamination_tests = delamination_tests.filter(sample_width__gte=sample_width_from).order_by('test_number')
			if form.cleaned_data.get('sample_width_to'):
				sample_width_to = form.cleaned_data.get('sample_width_to')
				delamination_tests = delamination_tests.filter(sample_width__lte=sample_width_to).order_by('test_number')
			if form.cleaned_data.get('sample_length_from'):
				sample_length_from = form.cleaned_data.get('sample_length_from')
				delamination_tests = delamination_tests.filter(sample_length__gte=sample_length_from).order_by('test_number')
			if form.cleaned_data.get('sample_length_to'):
				sample_length_to = form.cleaned_data.get('sample_length_to')
				delamination_tests = delamination_tests.filter(sample_length__lte=sample_length_to).order_by('test_number')
			if form.cleaned_data.get('glue_use_amount_from'):
				glue_use_amount_from = form.cleaned_data.get('glue_use_amount_from')
				delamination_tests = delamination_tests.filter(glue_use_amount__gte=glue_use_amount_from).order_by('test_number')
			if form.cleaned_data.get('glue_use_amount_to'):
				glue_use_amount_to = form.cleaned_data.get('glue_use_amount_to')
				delamination_tests = delamination_tests.filter(glue_use_amount__lte=glue_use_amount_to).order_by('test_number')
			if form.cleaned_data.get('glue_pressure_from'):
				glue_pressure_from = form.cleaned_data.get('glue_pressure_from')
				delamination_tests = delamination_tests.filter(glue_pressure__gte=glue_pressure_from).order_by('test_number')
			if form.cleaned_data.get('glue_pressure_to'):
				glue_pressure_to = form.cleaned_data.get('glue_pressure_to')
				delamination_tests = delamination_tests.filter(glue_pressure__lte=glue_pressure_to).order_by('test_number')
			if form.cleaned_data.get('start_glue_time_from'):
				start_glue_time_from = form.cleaned_data.get('start_glue_time_from')
				delamination_tests = delamination_tests.filter(start_glue_time__gte=start_glue_time_from).order_by('test_number')
			if form.cleaned_data.get('start_glue_time_to'):
				start_glue_time_to = form.cleaned_data.get('start_glue_time_to')
				delamination_tests = delamination_tests.filter(start_glue_time__lte=start_glue_time_to).order_by('test_number')
			if form.cleaned_data.get('pressure_time_from'):
				pressure_time_from = form.cleaned_data.get('pressure_time_from')
				delamination_tests = delamination_tests.filter(pressure_time__gte=pressure_time_from).order_by('test_number')
			if form.cleaned_data.get('pressure_time_to'):
				pressure_time_to = form.cleaned_data.get('pressure_time_to')
				delamination_tests = delamination_tests.filter(pressure_time__lte=pressure_time_to).order_by('test_number')
			if form.cleaned_data.get('layer_out_percent_from'):
				layer_out_percent_from = form.cleaned_data.get('layer_out_percent_from')
				delamination_tests = delamination_tests.filter(layer_out_percent__gte=layer_out_percent_from).order_by('test_number')
			if form.cleaned_data.get('layer_out_percent_to'):
				layer_out_percent_to = form.cleaned_data.get('layer_out_percent_to')
				delamination_tests = delamination_tests.filter(layer_out_percent__lte=layer_out_percent_to).order_by('test_number')
			if form.cleaned_data.get('passed_true'):
				delamination_tests = delamination_tests.filter(passed=True).order_by('test_number')
			if form.cleaned_data.get('passed_false'):
				delamination_tests = delamination_tests.filter(passed=False).order_by('test_number')
			if form.cleaned_data.get('comment'):
				comment = form.cleaned_data.get('comment')
				delamination_tests = delamination_tests.filter(comment__icontains=comment).order_by('test_number')

	else:
		form = DelaminationTestFilterForm()
	return render(request, 'mainApp/delamination_testsfilter.html', {'delamination_tests': delamination_tests, 
		'form': form, })


@login_required
def ShearTestfilterView(request):
	user = get_object_or_404(User, username=request.user.username)
	shear_tests = TestShear.objects.filter(author=user).order_by('test_number')
	if request.method == 'POST':
		form = ShearTestFilterForm(request.POST)
		if form.is_valid():
			if form.cleaned_data.get('start_test_date'):
				start_test_date = form.cleaned_data.get('start_test_date')
				shear_tests = shear_tests.filter(test_date__gte=start_test_date).order_by('test_number')
			if form.cleaned_data.get('end_test_date'):
				end_test_date = form.cleaned_data.get('end_test_date')
				shear_tests = shear_tests.filter(test_date__lte=end_test_date).order_by('test_number')
			if form.cleaned_data.get('test_number'):
				test_number = form.cleaned_data.get('test_number')
				shear_tests = shear_tests.filter(test_number=test_number).order_by('test_number')
			if form.cleaned_data.get('equipment'):
				equipment = form.cleaned_data.get('equipment')
				shear_tests = shear_tests.filter(equipment__iexact=equipment).order_by('test_number')
			if form.cleaned_data.get('type_of_wood'):
				type_of_wood = form.cleaned_data.get('type_of_wood')
				shear_tests = shear_tests.filter(type_of_wood=type_of_wood).order_by('test_number')
			if form.cleaned_data.get('timber_params'):
				timber_params = form.cleaned_data.get('timber_params')
				shear_tests = shear_tests.filter(timber_params__iexact=timber_params).order_by('test_number')
			if form.cleaned_data.get('sorter_person'):
				sorter_person = form.cleaned_data.get('sorter_person')
				shear_tests = shear_tests.filter(sorter_person=sorter_person).order_by('test_number')
			if form.cleaned_data.get('fj_person'):
				fj_person = form.cleaned_data.get('fj_person')
				shear_tests = shear_tests.filter(fj_person=fj_person).order_by('test_number')
			if form.cleaned_data.get('glue_person'):
				glue_person = form.cleaned_data.get('glue_person')
				shear_tests = shear_tests.filter(glue_person=glue_person).order_by('test_number')
			if form.cleaned_data.get('marking_person'):
				marking_person = form.cleaned_data.get('marking_person')
				shear_tests = shear_tests.filter(marking_person=marking_person).order_by('test_number')
			if form.cleaned_data.get('air_moisture_from'):
				air_moisture_from = form.cleaned_data.get('air_moisture_from')
				shear_tests = shear_tests.filter(air_moisture__gte=air_moisture_from).order_by('test_number')
			if form.cleaned_data.get('air_moisture_to'):
				air_moisture_to = form.cleaned_data.get('air_moisture_to')
				shear_tests = shear_tests.filter(air_moisture__lte=air_moisture_to).order_by('test_number')
			if form.cleaned_data.get('wood_moisture_from'):
				wood_moisture_from = form.cleaned_data.get('wood_moisture_from')
				shear_tests = shear_tests.filter(wood_moisture__gte=wood_moisture_from).order_by('test_number')
			if form.cleaned_data.get('wood_moisture_to'):
				wood_moisture_to = form.cleaned_data.get('wood_moisture_to')
				shear_tests = shear_tests.filter(wood_moisture__lte=wood_moisture_to).order_by('test_number')
			if form.cleaned_data.get('glue_harderner_amount'):
				glue_harderner_amount = form.cleaned_data.get('glue_harderner_amount')
				shear_tests = shear_tests.filter(glue_harderner_amount__iexact=glue_harderner_amount).order_by('test_number')
			if form.cleaned_data.get('air_temperature_from'):
				air_temperature_from = form.cleaned_data.get('air_temperature_from')
				shear_tests = shear_tests.filter(air_temperature__gte=air_temperature_from).order_by('test_number')
			if form.cleaned_data.get('air_temperature_to'):
				air_temperature_to = form.cleaned_data.get('air_temperature_to')
				shear_tests = shear_tests.filter(air_temperature__lte=air_temperature_to).order_by('test_number')
			if form.cleaned_data.get('wood_temperature_from'):
				wood_temperature_from = form.cleaned_data.get('wood_temperature_from')
				shear_tests = shear_tests.filter(wood_temperature__gte=wood_temperature_from).order_by('test_number')
			if form.cleaned_data.get('wood_temperature_to'):
				wood_temperature_to = form.cleaned_data.get('wood_temperature_to')
				shear_tests = shear_tests.filter(wood_temperature__lte=wood_temperature_to).order_by('test_number')
			if form.cleaned_data.get('glue'):
				glue = form.cleaned_data.get('glue')
				shear_tests = shear_tests.filter(glue__iexact=glue).order_by('test_number')
			if form.cleaned_data.get('glue_batch_number'):
				glue_batch_number = form.cleaned_data.get('glue_batch_number')
				shear_tests = shear_tests.filter(glue_batch_number=glue_batch_number).order_by('test_number')
			if form.cleaned_data.get('start_glue_expiration_date'):
				start_glue_expiration_date = form.cleaned_data.get('start_glue_expiration_date')
				shear_tests = shear_tests.filter(glue_expiration_date__gte=start_glue_expiration_date).order_by('test_number')
			if form.cleaned_data.get('end_glue_expiration_date'):
				end_glue_expiration_date = form.cleaned_data.get('end_glue_expiration_date')
				shear_tests = shear_tests.filter(glue_expiration_date__lte=end_glue_expiration_date).order_by('test_number')
			if form.cleaned_data.get('sample_thickness_from'):
				sample_thickness_from = form.cleaned_data.get('sample_thickness_from')
				shear_tests = shear_tests.filter(sample_thickness__gte=sample_thickness_from).order_by('test_number')
			if form.cleaned_data.get('sample_thickness_to'):
				sample_thickness_to = form.cleaned_data.get('sample_thickness_to')
				shear_tests = shear_tests.filter(sample_thickness__lte=sample_thickness_to).order_by('test_number')
			if form.cleaned_data.get('sample_width_from'):
				sample_width_from = form.cleaned_data.get('sample_width_from')
				shear_tests = shear_tests.filter(sample_width__gte=sample_width_from).order_by('test_number')
			if form.cleaned_data.get('sample_width_to'):
				sample_width_to = form.cleaned_data.get('sample_width_to')
				shear_tests = shear_tests.filter(sample_width__lte=sample_width_to).order_by('test_number')
			if form.cleaned_data.get('sample_length_from'):
				sample_length_from = form.cleaned_data.get('sample_length_from')
				shear_tests = shear_tests.filter(sample_length__gte=sample_length_from).order_by('test_number')
			if form.cleaned_data.get('sample_length_to'):
				sample_length_to = form.cleaned_data.get('sample_length_to')
				shear_tests = shear_tests.filter(sample_length__lte=sample_length_to).order_by('test_number')
			if form.cleaned_data.get('glue_use_amount_from'):
				glue_use_amount_from = form.cleaned_data.get('glue_use_amount_from')
				shear_tests = shear_tests.filter(glue_use_amount__gte=glue_use_amount_from).order_by('test_number')
			if form.cleaned_data.get('glue_use_amount_to'):
				glue_use_amount_to = form.cleaned_data.get('glue_use_amount_to')
				shear_tests = shear_tests.filter(glue_use_amount__lte=glue_use_amount_to).order_by('test_number')
			if form.cleaned_data.get('glue_pressure_from'):
				glue_pressure_from = form.cleaned_data.get('glue_pressure_from')
				shear_tests = shear_tests.filter(glue_pressure__gte=glue_pressure_from).order_by('test_number')
			if form.cleaned_data.get('glue_pressure_to'):
				glue_pressure_to = form.cleaned_data.get('glue_pressure_to')
				shear_tests = shear_tests.filter(glue_pressure__lte=glue_pressure_to).order_by('test_number')
			if form.cleaned_data.get('start_glue_time_from'):
				start_glue_time_from = form.cleaned_data.get('start_glue_time_from')
				shear_tests = shear_tests.filter(start_glue_time__gte=start_glue_time_from).order_by('test_number')
			if form.cleaned_data.get('start_glue_time_to'):
				start_glue_time_to = form.cleaned_data.get('start_glue_time_to')
				shear_tests = shear_tests.filter(start_glue_time__lte=start_glue_time_to).order_by('test_number')
			if form.cleaned_data.get('pressure_time_from'):
				pressure_time_from = form.cleaned_data.get('pressure_time_from')
				shear_tests = shear_tests.filter(pressure_time__gte=pressure_time_from).order_by('test_number')
			if form.cleaned_data.get('pressure_time_to'):
				pressure_time_to = form.cleaned_data.get('pressure_time_to')
				shear_tests = shear_tests.filter(pressure_time__lte=pressure_time_to).order_by('test_number')
			if form.cleaned_data.get('layer_ripped_percent_average_from'):
				layer_ripped_percent_average_from = form.cleaned_data.get('layer_ripped_percent_average_from')
				shear_tests = shear_tests.filter(layer_ripped_percent_average__gte=layer_ripped_percent_average_from).order_by('test_number')
			if form.cleaned_data.get('layer_ripped_percent_average_to'):
				layer_ripped_percent_average_to = form.cleaned_data.get('layer_ripped_percent_average_to')
				shear_tests = shear_tests.filter(layer_ripped_percent_average__lte=layer_ripped_percent_average_to).order_by('test_number')
			if form.cleaned_data.get('force_crash_from'):
				force_crash_from = form.cleaned_data.get('force_crash_from')
				shear_tests = shear_tests.filter(force_crash__gte=force_crash_from).order_by('test_number')
			if form.cleaned_data.get('force_crash_to'):
				force_crash_to = form.cleaned_data.get('force_crash_to')
				shear_tests = shear_tests.filter(force_crash__lte=force_crash_to).order_by('test_number')
			if form.cleaned_data.get('passed_true'):
				shear_tests = shear_tests.filter(passed=True).order_by('test_number')
			if form.cleaned_data.get('passed_false'):
				shear_tests = shear_tests.filter(passed=False).order_by('test_number')
			if form.cleaned_data.get('comment'):
				comment = form.cleaned_data.get('comment')
				shear_tests = shear_tests.filter(comment__icontains=comment).order_by('test_number')

	else:
		form = ShearTestFilterForm()
	return render(request, 'mainApp/shear_testsfilter.html', {'shear_tests': shear_tests, 
		'form': form, })

@login_required
def SettingsView(request):
	if request.method == 'POST':
		wood_form = Wood_typeForm(request.POST, prefix='wood_type')
		
		if wood_form.is_valid():
			wood_form.instance.author = request.user
			wood_form.save()
			messages.success(request, f'Новая порода дерева добавлена!')
			return redirect('settings')
		
	else:
		wood_form = Wood_typeForm(prefix='wood_type')
	if request.method == 'POST' and not wood_form.is_valid():
		class_form = strength_class_typesForm(request.POST, prefix='strength_class')
		wood_form = Wood_typeForm(prefix='wood_type')
		if class_form.is_valid():
			class_form.instance.author = request.user
			class_form.save()
			messages.success(request, f'Новый класс прочности добавлен!')
			return redirect('settings')
	else:
		class_form = strength_class_typesForm(prefix='strength_class')
	user = get_object_or_404(User, username=request.user.username)
	wood_types_list = Wood_types.objects.filter(author=user).order_by('name')
	class_strength_list = strength_class_types.objects.filter(author=user).order_by('name')
	return render(request, 'mainApp/settings.html', {'wood_form': wood_form, 'class_form': class_form,
		'wood_types_list': wood_types_list, 'class_strength_list': class_strength_list})

class Wood_types_UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Wood_types
	success_url = '/settings'
	template_name = 'mainApp/wood_types_update.html'
	form_class = Wood_typeForm
	#fields = ['name',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Порода дерева сохранена!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		wood_type = self.get_object()
		if self.request.user == wood_type.author:
			return True
		return False

class Wood_types_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Wood_types
	success_url = '/settings'
	template_name = 'mainApp/wood_types_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Порода дерева удалена!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		wood_type = self.get_object()
		if self.request.user == wood_type.author:
			return True
		return False

class Wood_types_DetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Wood_types

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False


class Strength_class_UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = strength_class_types
	success_url = '/settings'
	template_name = 'mainApp/strength_class_update.html'
	form_class = strength_class_typesForm
	#fields = ['name',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Класс прочности сохранен!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		strength_class_type = self.get_object()
		if self.request.user == strength_class_type.author:
			return True
		return False

class Strength_class_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = strength_class_types
	success_url = '/settings'
	template_name = 'mainApp/strength_class_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Класс прочности удален!')
		return super().post(request, *args, **kwargs)

	def test_func(self):
		strength_class_type = self.get_object()
		if self.request.user == strength_class_type.author:
			return True
		return False


class Strength_class_DetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = strength_class_types

	def test_func(self):
		test = self.get_object()
		if self.request.user == test.author:
			return True
		return False
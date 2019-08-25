from django.shortcuts import render, redirect, get_object_or_404
from .forms import BendtestForm, TestDelaminationForm, TestShearForm, DateForm, NonconformityForm, PersonForm, ToolForm, BendtestFilterForm
from django.contrib import messages
from .models import TestLamella, TestDelamination, TestShear, Nonconformity, Person, Tool
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
	success_url = '/'
	form_class = BendtestForm
	template_name = 'mainApp/TestUpdate.html'
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
	success_url = '/'
	form_class = TestDelaminationForm
	template_name = 'mainApp/TestUpdate.html'
	'''fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_harderner_amount', 
		'glue_temperature', 'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'layer_out_percent', 'passed', 'comment', 'photo',]'''

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Тест на деламинацию был изменен!')
		return super().post(request, *args, **kwargs)

class ShearTestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = TestShear
	success_url = '/'
	template_name = 'mainApp/TestUpdate.html'
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

class BendTestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = TestLamella
	success_url = '/'
	template_name = 'mainApp/test_confirm_delete.html'

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


class NonconformityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Nonconformity
	success_url = '/nonconformities'
	template_name = 'mainApp/nonconformity_update.html'
	fields = ['name', 'description', 'resp_person', 'nonconformity_date',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Несоответствие отредактировано!')
		return super().post(request, *args, **kwargs)

class NonconformityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Nonconformity
	success_url = '/nonconformities'
	template_name = 'mainApp/nonconformity_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Несоответствие удалено!')
		return super().post(request, *args, **kwargs)	

class NonconformityDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Nonconformity

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
	fields = ['name', 'position', 'training_date', 'next_training_date', 'comment',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Данные о сотруднике сохранены!')
		return super().post(request, *args, **kwargs)

class PersonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Person
	success_url = '/persons'
	template_name = 'mainApp/person_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Данные о сотруднике удалены!')
		return super().post(request, *args, **kwargs)

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

@login_required
def ToolsView(request):
	user = get_object_or_404(User, username=request.user.username)
	tools = Tool.objects.filter(author=user).order_by('name')
	return render(request, 'mainApp/tools.html', {'tools': tools,})

class ToolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Tool
	success_url = '/tools'
	template_name = 'mainApp/tool_update.html'
	fields = ['name', 'description', 'resp_person', 'calibration_date', 'next_calibration_date',]

	def post(self, request, *args, **kwargs):
		messages.success(request, f'Информация сохранена!')
		return super().post(request, *args, **kwargs)


class ToolDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Tool
	success_url = '/tools'
	template_name = 'mainApp/tool_confirm_delete.html'
	
	def post(self, request, *args, **kwargs):
		messages.success(request, f'Данные удалены!')
		return super().post(request, *args, **kwargs)

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


	else:
		form = BendtestFilterForm()
	return render(request, 'mainApp/bendtestfilter.html', {'bendtests': bendtests, 'form': form, })
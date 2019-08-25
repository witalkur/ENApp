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
				bendtests = bendtests.filter(type_of_wood__in=type_of_wood).order_by('test_number')
	else:
		form = BendtestFilterForm()
	return render(request, 'mainApp/bendtestfilter.html', {'bendtests': bendtests, 'form': form, })
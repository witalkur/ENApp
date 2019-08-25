from django import forms
from .models import TestLamella, TestDelamination, TestShear, Nonconformity, Person, Tool, Wood_types
import datetime
from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus import TimePickerInput
from .models import def_bt_glue_expiration_date, def_d_glue_expiration_date, def_sh_glue_expiration_date


class BendtestForm(forms.ModelForm):
	test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today())
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=def_bt_glue_expiration_date)

	class Meta:
		model = TestLamella
		fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'strength_class', 'glue', 
		'glue_harderner_amount', 'lamellas_thickness', 'lamellas_width', 'lamellas_length', 'fj_length', 'fj_path', 'fj_gap',
		'fj_angle', 'fj_orientation', 'lamellas_left_moisture', 'lamellas_right_moisture', 'glue_pressure',
		'pressure_time', 'glue_use_amount', 'glue_batch_number', 'glue_expiration_date', 'lamellas_param',
		'lamellas_took_person', 'force_crash', 'time_of_testing', 'lamellas_strength', 'passed', 'by_fj_crash', 'base_fj_crash',
		'out_of_fj_crash', 'comment', 'photo']

class TestDelaminationForm(forms.ModelForm):
	test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today())
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=def_d_glue_expiration_date)

	class Meta:
		model = TestDelamination
		fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_harderner_amount', 
		'glue_temperature', 'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'layer_out_percent', 'passed', 'comment', 'photo',]


class TestShearForm(forms.ModelForm):
	test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today())
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=def_sh_glue_expiration_date)

	class Meta:
		model = TestShear
		fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_temperature',
		'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_harderner_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'time_of_testing', 'layer_ripped_percent1', 'layer_ripped_percent2',
		 'layer_ripped_percent3', 'layer_ripped_percent4', 'layer_ripped_percent5', 'layer_ripped_percent_average',
		 'force_crash', 'passed', 'comment', 'photo']


class DateForm(forms.Form):
	need_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

class NonconformityForm(forms.ModelForm):
	nonconformity_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

	class Meta:
		model = Nonconformity
		fields = ['name', 'description', 'resp_person', 'nonconformity_date',]

class PersonForm(forms.ModelForm):
	training_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
	next_training_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

	class Meta:
		model = Person
		fields = ['name', 'position', 'training_date', 'next_training_date', 'comment',]

class ToolForm(forms.ModelForm):
	calibration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
	next_calibration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

	class Meta:
		model = Tool
		fields = ['name', 'description', 'resp_person', 'calibration_date', 'next_calibration_date',]

wood_types = [('', '-------'), ('spruce', 'spruce'), ('pine', 'pine')]
#wood_types = ['spruce', 'pine',]
strength_class_types = [('', '-------'), ('C14', 'C14'), ('C18', 'C18'), ('C24', 'C24'), ('C30', 'C30')]
fj_orientation_types = [('', '-------'), ('Пластевое', 'Пластевое'), ('Ребровое', 'Ребровое')]
class BendtestFilterForm(forms.ModelForm):
	start_test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today(),required=False)
	end_test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today(), required=False)
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=def_bt_glue_expiration_date, required=False)
	lamellas_took_person = forms.ModelChoiceField(queryset=Person.objects.all(), initial=None, required=False)
	test_number = forms.IntegerField(initial=None, required=False)
	equipment = forms.CharField(max_length=100, initial=None, required=False)
	type_of_wood = forms.ModelMultipleChoiceField(queryset=Wood_types.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
	#type_of_wood = forms.MultipleChoiceField(choices=wood_types, required=False)
	strength_class = forms.ChoiceField(choices=strength_class_types, initial='', widget=forms.Select(), required=False)
	glue = forms.CharField(max_length=100, initial=None, required=False)
	glue_harderner_amount = forms.CharField(max_length=100, initial=None, required=False)
	lamellas_thickness = forms.IntegerField(initial=None, required=False)
	lamellas_width = forms.IntegerField(initial=None, required=False)
	lamellas_length = forms.IntegerField(initial=None, required=False)
	fj_length = forms.IntegerField(initial=None, required=False)
	fj_path = forms.IntegerField(initial=None, required=False)
	fj_gap = forms.IntegerField(initial=None, required=False)
	fj_angle = forms.IntegerField(initial=None, required=False)
	fj_orientation = forms.ChoiceField(choices=fj_orientation_types, initial='', widget=forms.Select(), required=False)
	lamellas_left_moisture = forms.IntegerField(initial=None, required=False)
	lamellas_right_moisture = forms.IntegerField(initial=None, required=False)
	glue_pressure = forms.FloatField(initial=None, required=False)
	pressure_time = forms.IntegerField(initial=None, required=False)
	glue_use_amount = forms.IntegerField(initial=None, required=False)
	glue_batch_number = forms.CharField(max_length=100, initial=None, required=False)
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=None,required=False)
	lamellas_param = forms.CharField(max_length=100, initial=None, required=False)
	force_crash = forms.FloatField(initial=None, required=False)
	start_test_time = forms.TimeField(widget=TimePickerInput(), initial=None, required=False)
	end_test_time = forms.TimeField(widget=TimePickerInput(), initial=None, required=False)
	lamellas_strength = forms.FloatField(initial=None, required=False)
	by_fj_crash = forms.IntegerField(initial=None, required=False)
	base_fj_crash = forms.IntegerField(initial=None, required=False)
	out_of_fj_crash = forms.IntegerField(initial=None, required=False)
	comment = forms.CharField(widget=forms.Textarea, max_length=400, initial=None, required=False)

	class Meta:
		model = TestLamella
		fields = ['start_test_date', 'end_test_date', 'start_test_time', 'start_test_time', 'end_test_time', 'test_number', 'equipment', 'type_of_wood', 'strength_class', 'glue', 
		'glue_harderner_amount', 'lamellas_thickness', 'lamellas_width', 'lamellas_length', 'fj_length', 'fj_path', 'fj_gap',
		'fj_angle', 'fj_orientation', 'lamellas_left_moisture', 'lamellas_right_moisture', 'glue_pressure',
		'pressure_time', 'glue_use_amount', 'glue_batch_number', 'glue_expiration_date', 'lamellas_param',
		'lamellas_took_person', 'force_crash', 'time_of_testing', 'lamellas_strength', 'passed', 'by_fj_crash', 'base_fj_crash',
		'out_of_fj_crash', 'comment']
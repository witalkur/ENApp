from django import forms
from .models import TestLamella, TestDelamination, TestShear, Nonconformity, Person, Tool, Wood_types, strength_class_types
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

class Wood_typeForm(forms.ModelForm):
	name = forms.CharField(max_length=100)

	class Meta:
		model = Wood_types
		fields = ['name']

class strength_class_typesForm(forms.ModelForm):
	name = forms.CharField(max_length=100)

	class Meta:
		model = strength_class_types
		fields = ['name']

class ToolForm(forms.ModelForm):
	calibration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
	next_calibration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

	class Meta:
		model = Tool
		fields = ['name', 'description', 'resp_person', 'calibration_date', 'next_calibration_date',]

#wood_types = [('', '-------'), ('spruce', 'spruce'), ('pine', 'pine')]
#wood_types = ['spruce', 'pine',]
#strength_class_types = [('', '-------'), ('C14', 'C14'), ('C18', 'C18'), ('C24', 'C24'), ('C30', 'C30')]
fj_orientation_types = [('', '-------'), ('Пластевое', 'Пластевое'), ('Ребровое', 'Ребровое')]

class BendtestFilterForm(forms.ModelForm):
	start_test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=None,required=False)
	end_test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today(), required=False)
	lamellas_took_person = forms.ModelChoiceField(queryset=Person.objects.all(), initial=None, required=False)
	test_number = forms.IntegerField(initial=None, required=False)
	equipment = forms.CharField(max_length=100, initial=None, required=False)
	type_of_wood = forms.ModelChoiceField(queryset=Wood_types.objects.all(), initial='None', required=False)
	strength_class = forms.ModelChoiceField(queryset=strength_class_types.objects.all(), initial='None', required=False)
	glue = forms.CharField(max_length=100, initial=None, required=False)
	glue_harderner_amount = forms.CharField(max_length=100, initial=None, required=False)
	lamellas_thickness_from = forms.IntegerField(initial=None, required=False)
	lamellas_thickness_to = forms.IntegerField(initial=None, required=False)
	lamellas_width_from = forms.IntegerField(initial=None, required=False)
	lamellas_width_to = forms.IntegerField(initial=None, required=False)
	lamellas_length_from = forms.IntegerField(initial=None, required=False)
	lamellas_length_to = forms.IntegerField(initial=None, required=False)
	fj_length = forms.IntegerField(initial=None, required=False)
	fj_path = forms.IntegerField(initial=None, required=False)
	fj_gap = forms.IntegerField(initial=None, required=False)
	fj_angle = forms.IntegerField(initial=None, required=False)
	fj_orientation = forms.ChoiceField(choices=fj_orientation_types, initial='', widget=forms.Select(), required=False)
	lamellas_left_moisture_from = forms.IntegerField(initial=None, required=False)
	lamellas_left_moisture_to = forms.IntegerField(initial=None, required=False)
	lamellas_right_moisture_from = forms.IntegerField(initial=None, required=False)
	lamellas_right_moisture_to = forms.IntegerField(initial=None, required=False)
	glue_pressure_from = forms.FloatField(initial=None, required=False)
	glue_pressure_to = forms.FloatField(initial=None, required=False)
	pressure_time_from = forms.IntegerField(initial=None, required=False)
	pressure_time_to = forms.IntegerField(initial=None, required=False)
	glue_use_amount_from = forms.IntegerField(initial=None, required=False)
	glue_use_amount_to = forms.IntegerField(initial=None, required=False)
	glue_batch_number = forms.CharField(max_length=100, initial=None, required=False)
	start_glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=None, required=False)
	end_glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=None, required=False)
	lamellas_param = forms.CharField(max_length=100, initial=None, required=False)
	force_crash_from = forms.FloatField(initial=None, required=False)
	force_crash_to = forms.FloatField(initial=None, required=False)
	start_test_time = forms.TimeField(widget=TimePickerInput(), initial=None, required=False)
	end_test_time = forms.TimeField(widget=TimePickerInput(), initial=None, required=False)
	time_of_testing_from = forms.IntegerField(initial=None, required=False)
	time_of_testing_to = forms.IntegerField(initial=None, required=False)
	lamellas_strength_from = forms.FloatField(initial=None, required=False)
	lamellas_strength_to = forms.FloatField(initial=None, required=False)
	by_fj_crash_from = forms.IntegerField(initial=None, required=False)
	by_fj_crash_to = forms.IntegerField(initial=None, required=False)
	base_fj_crash_from = forms.IntegerField(initial=None, required=False)
	base_fj_crash_to = forms.IntegerField(initial=None, required=False)
	out_of_fj_crash_from = forms.IntegerField(initial=None, required=False)
	out_of_fj_crash_to = forms.IntegerField(initial=None, required=False)
	passed_true = forms.BooleanField(initial=False, required=False)
	passed_false = forms.BooleanField(initial=False, required=False)
	comment = forms.CharField(widget=forms.Textarea, max_length=400, initial=None, required=False)

	class Meta:
		model = TestLamella
		fields = ['start_test_date', 'end_test_date', 'start_test_time', 'start_test_time', 'end_test_time', 'test_number', 
		'equipment', 'type_of_wood', 'strength_class', 'glue', 
		'glue_harderner_amount', 'lamellas_thickness_from', 'lamellas_thickness_to', 'lamellas_width_from', 
		'lamellas_width_to', 'lamellas_length_from', 'lamellas_length_to', 'fj_length', 'fj_path', 'fj_gap',
		'fj_angle', 'fj_orientation', 'lamellas_left_moisture_from', 'lamellas_left_moisture_to',
		'lamellas_right_moisture_from', 'lamellas_right_moisture_to', 'glue_pressure_from', 'glue_pressure_to',
		'pressure_time_from', 'pressure_time_to', 'glue_use_amount_from', 'glue_use_amount_to', 
		'glue_batch_number', 'start_glue_expiration_date', 'end_glue_expiration_date', 'lamellas_param',
		'lamellas_took_person', 'force_crash_from', 'force_crash_to', 'time_of_testing_from', 'time_of_testing_to',
		 'lamellas_strength_from', 'lamellas_strength_to', 'passed', 'by_fj_crash_from', 'by_fj_crash_to', 
		'base_fj_crash_from', 'base_fj_crash_to', 'out_of_fj_crash_from', 'out_of_fj_crash_to', 'passed_true', 
		'passed_false', 'comment']
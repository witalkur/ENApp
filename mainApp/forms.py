from django import forms
from .models import TestLamella, TestDelamination, TestShear, Nonconformity, Person, Tool, glue_expiration_date_1
import datetime
from bootstrap_datepicker_plus import DatePickerInput


class BendtestForm(forms.ModelForm):
	test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=datetime.date.today())
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), initial=glue_expiration_date_1)

	class Meta:
		model = TestLamella
		fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'strength_class', 'glue', 
		'glue_harderner_amount', 'lamellas_thickness', 'lamellas_width', 'lamellas_length', 'fj_length', 'fj_path', 'fj_gap',
		'fj_angle', 'fj_orientation', 'lamellas_left_moisture', 'lamellas_right_moisture', 'glue_pressure',
		'pressure_time', 'glue_use_amount', 'glue_batch_number', 'glue_expiration_date', 'lamellas_param',
		'lamellas_took_person', 'force_crash', 'time_of_testing', 'lamellas_strength', 'passed', 'by_fj_crash', 'base_fj_crash',
		'out_of_fj_crash', 'comment', 'photo']

class TestDelaminationForm(forms.ModelForm):
	test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

	class Meta:
		model = TestDelamination
		fields = ['test_date', 'test_time', 'test_number', 'equipment', 'type_of_wood', 'timber_params', 'sorter_person',
		'fj_person', 'glue_person', 'marking_person', 'air_moisture', 'wood_moisture', 'glue_harderner_amount', 
		'glue_temperature', 'air_temperature', 'wood_temperature', 'glue', 'glue_batch_number', 'glue_expiration_date',
		'sample_thickness', 'sample_width', 'sample_length', 'glue_use_amount', 'glue_pressure',
		'start_glue_time', 'end_glue_time', 'pressure_time', 'layer_out_percent', 'passed', 'comment', 'photo',]


class TestShearForm(forms.ModelForm):
	test_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
	glue_expiration_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

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


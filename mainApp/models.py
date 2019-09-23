from django.db import models
from PIL import Image
import datetime
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
'''
from .bendtest_function import (def_bt_equipment, def_bt_glue, def_bt_lamellas_thickness,
def_bt_lamellas_width, def_bt_lamellas_length, def_bt_glue_harderner_amount, def_bt_test_number,
def_bt_test_time, def_bt_fj_length, def_bt_fj_path, def_bt_fj_gap, def_bt_fj_angle, def_bt_type_of_wood,
def_bt_strength_class, def_bt_fj_orientation, def_bt_lamellas_left_moisture, def_bt_lamellas_right_moisture,
def_bt_glue_pressure, def_bt_pressure_time, def_bt_glue_use_amount, def_bt_glue_batch_number, 
def_bt_lamellas_param, def_bt_glue_expiration_date, def_bt_lamellas_took_person)

from .delam_functions import (def_d_equipment, def_d_glue, def_d_glue_harderner_amount, def_d_test_number,
def_d_test_time, def_d_type_of_wood, def_d_glue_pressure, def_d_pressure_time, def_d_glue_use_amount,
def_d_glue_batch_number, def_d_air_moisture, def_d_timber_params, def_d_sorter_person, def_d_fj_person,
def_d_glue_person, def_d_marking_person, def_d_glue_expiration_date, def_d_wood_moisture, def_d_glue_temperature,
def_d_wood_temperature, def_d_air_temperature)
'''
#wood_types = [('spruce', 'spruce'), ('pine', 'pine')]
#strength_class_types = [('C14', 'C14'), ('C18', 'C18'), ('C24', 'C24'), ('C30', 'C30')]


def def_d_equipment():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.equipment
	except: return None

def def_d_glue():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue
	except: return None

def def_d_glue_harderner_amount():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_harderner_amount
	except: return None

def def_d_test_number():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return (int(last_delamtests.test_number) + 1)
	except: return None

def def_d_test_time():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.test_time
	except: return None

def def_d_type_of_wood():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.type_of_wood
	except: return None

def def_d_glue_pressure():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_pressure
	except: return None

def def_d_pressure_time():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.pressure_time
	except: return None

def def_d_glue_use_amount():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_use_amount
	except: return None

def def_d_glue_batch_number():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_batch_number
	except: return None

def def_d_air_moisture():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.air_moisture
	except: return None

def def_d_timber_params():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.timber_params
	except: return None

def def_d_sorter_person():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.sorter_person
	except: return None

def def_d_fj_person():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.fj_person
	except: return None

def def_d_glue_person():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_person
	except: return None

def def_d_marking_person():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.marking_person
	except: return None
	
def def_d_glue_expiration_date():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_expiration_date
	except: return None

def def_d_wood_moisture():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.wood_moisture
	except: return None

def def_d_glue_temperature():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.glue_temperature
	except: return None

def def_d_air_temperature():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.air_temperature
	except: return None

def def_d_wood_temperature():
	try:
		last_delamtests = TestDelamination.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_delamtests.wood_temperature
	except: return None
#lkjSDBvljbsv
def def_sh_equipment():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.equipment
	except: return None

def def_sh_glue():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue
	except: return None

def def_sh_glue_harderner_amount():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_harderner_amount
	except: return None

def def_sh_test_number():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return (int(last_sheartests.test_number) + 1)
	except: return None

def def_sh_test_time():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.test_time
	except: return None

def def_sh_type_of_wood():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.type_of_wood
	except: return None

def def_sh_glue_pressure():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_pressure
	except: return None

def def_sh_pressure_time():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.pressure_time
	except: return None

def def_sh_glue_use_amount():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_use_amount
	except: return None

def def_sh_glue_batch_number():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_batch_number
	except: return None

def def_sh_air_moisture():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.air_moisture
	except: return None

def def_sh_timber_params():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.timber_params
	except: return None

def def_sh_sorter_person():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.sorter_person
	except: return None

def def_sh_fj_person():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.fj_person
	except: return None

def def_sh_glue_person():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_person
	except: return None

def def_sh_marking_person():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.marking_person
	except: return None
	
def def_sh_glue_expiration_date():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_expiration_date
	except: return None

def def_sh_wood_moisture():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.wood_moisture
	except: return None

def def_sh_glue_temperature():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.glue_temperature
	except: return None

def def_sh_air_temperature():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.air_temperature
	except: return None

def def_sh_wood_temperature():
	try:
		last_sheartests = TestShear.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_sheartests.wood_temperature
	except: return None	

def def_bt_equipment():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.equipment
	except: return None

def def_bt_glue():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.glue
	except: return None

def def_bt_lamellas_thickness():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_thickness
	except: return None

def def_bt_lamellas_width():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_width
	except: return None

def def_bt_lamellas_length():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_length
	except: return None

def def_bt_glue_harderner_amount():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.glue_harderner_amount
	except: return None

def def_bt_test_number():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return (int(last_bendtests.test_number) + 1)
	except: return None

def def_bt_test_time():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.test_time
	except: return None

def def_bt_fj_length():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.fj_length
	except: return None

def def_bt_fj_path():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.fj_path
	except: return None

def def_bt_fj_gap():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.fj_gap
	except: return None

def def_bt_fj_angle():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.fj_angle
	except: return None

def def_bt_type_of_wood():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.type_of_wood
	except: return None

def def_bt_strength_class():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.strength_class
	except: return None

def def_bt_fj_orientation():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.fj_orientation
	except: return None

def def_bt_lamellas_left_moisture():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_left_moisture
	except: return None

def def_bt_lamellas_right_moisture():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_right_moisture
	except: return None

def def_bt_glue_pressure():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.glue_pressure
	except: return None

def def_bt_pressure_time():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.pressure_time
	except: return None

def def_bt_glue_use_amount():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.glue_use_amount
	except: return None

def def_bt_glue_batch_number():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.glue_batch_number
	except: return None

def def_bt_glue_expiration_date():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.glue_expiration_date
	except: return None

def def_bt_lamellas_param():
	try:
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_param
	except: return None

def def_bt_lamellas_took_person():
	try: 
		last_bendtests = TestLamella.objects.all().order_by('-test_date', '-test_number', '-test_time').first()
		return last_bendtests.lamellas_took_person
	except: return None

class Person(models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	training_date = models.DateField()
	next_training_date = models.DateField()
	comment = models.TextField(blank=True)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
#wood_types = [('', '-------'), ('spruce', 'spruce'), ('pine', 'pine')]

class Wood_types(models.Model):
	name = models.CharField(max_length=100)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class strength_class_types(models.Model):
	name = models.CharField(max_length=100)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class TestLamella(models.Model):
	test_date = models.DateField()
	test_time = models.TimeField(blank=True, null=True, default=None)
	test_number = models.IntegerField(default=def_bt_test_number)
	equipment = models.CharField(max_length=100, default=def_bt_equipment)
	type_of_wood = models.ForeignKey(Wood_types, on_delete=models.PROTECT, null=True, related_name='TestLamella_fj_wood_type', default=def_bt_type_of_wood)
	strength_class = models.ForeignKey(strength_class_types, on_delete=models.PROTECT, null=True, related_name='TestLamella_strength_class', default=def_bt_strength_class)
	glue = models.CharField(max_length=100, default=def_bt_glue)
	glue_harderner_amount = models.CharField(max_length=100, blank=True, default=def_bt_glue_harderner_amount)
	lamellas_thickness = models.IntegerField(default=def_bt_lamellas_thickness)
	lamellas_width = models.IntegerField(default=def_bt_lamellas_width)
	lamellas_length = models.IntegerField(default=def_bt_lamellas_length)
	fj_length = models.IntegerField(default=def_bt_fj_length)
	fj_path = models.IntegerField(default=def_bt_fj_path)
	fj_gap = models.IntegerField(default=def_bt_fj_gap)
	fj_angle = models.IntegerField(default=def_bt_fj_angle)
	fj_orientation = models.CharField(max_length=100, choices=[('Пластевое', 'Пластевое'), ('Ребровое', 'Ребровое')], default=def_bt_fj_orientation)
	lamellas_left_moisture = models.IntegerField(default=def_bt_lamellas_left_moisture)
	lamellas_right_moisture = models.IntegerField(default=def_bt_lamellas_right_moisture)
	glue_pressure = models.FloatField(default=def_bt_glue_pressure)
	pressure_time = models.IntegerField(blank=True, null=True, default=def_bt_pressure_time)
	glue_use_amount = models.IntegerField(default=def_bt_glue_use_amount)
	glue_batch_number = models.CharField(max_length=100, default=def_bt_glue_batch_number)
	glue_expiration_date = models.DateField()
	lamellas_param = models.CharField(blank=True, max_length=100, default=def_bt_lamellas_param)
	lamellas_took_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestLamella_took_person', default=def_bt_lamellas_took_person)
	force_crash = models.FloatField()
	time_of_testing = models.IntegerField(blank=True, null=True)
	lamellas_strength = models.FloatField()
	passed = models.BooleanField(default=False)
	by_fj_crash = models.IntegerField()
	base_fj_crash = models.IntegerField()
	out_of_fj_crash = models.IntegerField()
	comment = models.TextField(blank=True)
	photo = models.ImageField(upload_to='uploads', blank=True)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)




	def __str__(self):
		return (str(self.test_number) + '  Lamellas Test')

	#def save(self):
		#super().save()
		#img = Image.open(self.image.path)
		#if img.height > 600 or img.width > 600:
			#output_size = (600, 600)
			#img.thumbnail(output_size)
			#img.save(self.image.path)



class TestDelamination(models.Model):
	test_date = models.DateField()
	test_time = models.TimeField(blank=True, null=True, default=def_d_test_time)
	test_number = models.IntegerField(default=def_d_test_number)
	equipment = models.CharField(max_length=100, default=def_d_equipment)
	type_of_wood = models.ForeignKey(Wood_types, on_delete=models.PROTECT, related_name='TestDelamination_type_of_wood', default=def_d_type_of_wood)
	timber_params = models.CharField(max_length=100, default=def_d_timber_params)
	sorter_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_sorter_person', default=def_d_sorter_person)
	fj_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_fj_person', default=def_d_fj_person)
	glue_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_glue_person', default=def_d_glue_person)
	marking_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_marking_person', default=def_d_marking_person)
	air_moisture = models.IntegerField(default=def_d_air_moisture)
	wood_moisture = models.IntegerField(default=def_d_wood_moisture)
	glue_harderner_amount = models.CharField(max_length=100, blank=True, default=def_d_glue_harderner_amount)
	#glue_temperature = models.IntegerField(blank=True, null=True, default=def_d_glue_temperature)
	air_temperature = models.IntegerField(default=def_d_air_temperature)
	wood_temperature = models.IntegerField(blank=True, null=True, default=def_d_wood_temperature)
	glue = models.CharField(max_length=100, default=def_d_glue)
	glue_batch_number = models.CharField(max_length=100, default=def_d_glue_batch_number)
	glue_expiration_date = models.DateField()
	sample_thickness = models.FloatField()
	sample_width = models.FloatField()
	sample_length = models.FloatField()
	glue_use_amount = models.IntegerField(default=def_d_glue_use_amount)
	glue_pressure = models.FloatField(default=def_d_glue_pressure)
	start_glue_time = models.TimeField(blank=True, null=True)
	end_glue_time = models.TimeField(blank=True, null=True)
	pressure_time = models.IntegerField(blank=True, null=True)
	layer_out_percent = models.IntegerField()
	passed = models.BooleanField(default=False)
	comment = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to='uploads', blank=True)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return (str(self.test_number) + '  Delamination Test')



class TestShear(models.Model):
	test_date = models.DateField()
	test_time = models.TimeField(blank=True, null=True, default=None)
	test_number = models.IntegerField(default=def_sh_test_number)
	equipment = models.CharField(max_length=100, default=def_sh_equipment)
	type_of_wood = models.ForeignKey(Wood_types, on_delete=models.PROTECT, related_name='TestShear_type_of_wood', default=def_sh_type_of_wood)
	timber_params = models.CharField(max_length=100, default=def_sh_timber_params)
	sorter_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_sorter_person', default=def_sh_sorter_person)
	fj_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_fj_person', default=def_sh_fj_person)
	glue_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_glue_person', default=def_sh_glue_person)
	marking_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_marking_person', default=def_sh_marking_person)
	air_moisture = models.IntegerField(default=def_sh_air_moisture)
	wood_moisture = models.IntegerField(default=def_sh_wood_moisture)
	glue_temperature = models.IntegerField(blank=True, null=True, default=def_sh_glue_temperature)
	air_temperature = models.IntegerField(default=def_sh_air_temperature)
	wood_temperature = models.IntegerField(blank=True, null=True, default=def_sh_wood_temperature)
	glue = models.CharField(max_length=100, default=def_sh_glue)
	glue_batch_number = models.CharField(max_length=100, default=def_sh_glue_batch_number)
	glue_expiration_date = models.DateField(default=def_sh_glue_expiration_date)
	sample_thickness = models.IntegerField()
	sample_width = models.IntegerField()
	sample_length = models.IntegerField()
	glue_use_amount = models.IntegerField(default=def_sh_glue_use_amount)
	glue_harderner_amount = models.CharField(max_length=100, blank=True, default=def_sh_glue_harderner_amount)
	glue_pressure = models.FloatField(default=def_sh_glue_pressure)
	start_glue_time = models.TimeField(blank=True, null=True)
	end_glue_time = models.TimeField(blank=True, null=True)
	pressure_time = models.IntegerField(blank=True, null=True)
	time_of_testing = models.IntegerField(blank=True, null=True)
	number_of_layers = models.IntegerField()
	layer_ripped_percent_average = models.IntegerField()
	force_crash = models.FloatField()
	passed = models.BooleanField(default=False)
	comment = models.TextField(blank=True)
	photo = models.ImageField(upload_to='uploads', blank=True)
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return (str(self.test_number) + '  Shear Test')


class Nonconformity(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	resp_person = models.ForeignKey(Person, on_delete=models.PROTECT)
	nonconformity_date = models.DateField()
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Tool(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	resp_person = models.ForeignKey(Person, on_delete=models.PROTECT)
	calibration_date = models.DateField()
	next_calibration_date = models.DateField()
	author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


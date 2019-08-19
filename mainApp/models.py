from django.db import models
from PIL import Image
import datetime

wood_types = [('spruce', 'spruce'), ('pine', 'pine')]
strength_class_types = [('C14', 'C14'), ('C18', 'C18'), ('C24', 'C24'), ('C30', 'C30')]


def default_eq(x):
	last_bendtests = TestLamella.objects.all().order_by('-test_date').first()
	if x == 'equip':
		return last_bendtests.equipment
	elif x == 'glue':
		return last_bendtests.glue
	elif x == 'lamellas_thickness':
		return last_bendtests.lamellas_thickness
	elif x == 'lamellas_width':
		return last_bendtests.lamellas_width
	elif x == 'lamellas_length':
		return last_bendtests.lamellas_length
	elif x == 'glue_harderner_amount':
		return last_bendtests.glue_harderner_amount
	elif x == 'test_number':
		return (int(last_bendtests.test_number) + 1)
	elif x == 'test_time':
		return last_bendtests.test_time
	elif x == 'fj_length':
		return last_bendtests.fj_length
	elif x == 'fj_path':
		return last_bendtests.fj_path
	elif x == 'fj_gap':
		return last_bendtests.fj_gap
	elif x == 'fj_angle':
		return last_bendtests.fj_angle
	elif x == 'type_of_wood':
		return last_bendtests.type_of_wood
	elif x == 'strength_class':
		return last_bendtests.strength_class
	elif x == 'fj_orientation':
		return last_bendtests.fj_orientation
	elif x == 'lamellas_left_moisture':
		return last_bendtests.lamellas_left_moisture
	elif x == 'lamellas_right_moisture':
		return last_bendtests.lamellas_right_moisture
	elif x == 'glue_pressure':
		return last_bendtests.glue_pressure
	elif x == 'pressure_time':
		return last_bendtests.pressure_time
	elif x == 'glue_use_amount':
		return last_bendtests.glue_use_amount
	elif x == 'glue_batch_number':
		return last_bendtests.glue_batch_number
	elif x == 'glue_expiration_date':
		return last_bendtests.glue_expiration_date
	elif x == 'lamellas_param':
		return last_bendtests.lamellas_param
	elif x == 'lamellas_took_person':
		return last_bendtests.lamellas_took_person
	elif x == 'glue_expiration_date':
		glue_expiration_date_1 = last_bendtests.glue_expiration_date


class Person(models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	training_date = models.DateField()
	next_training_date = models.DateField()
	comment = models.TextField(blank=True)

	def __str__(self):
		return self.name

class TestLamella(models.Model):
	test_date = models.DateField()
	test_time = models.TimeField(blank=True, default=lambda: default_eq('test_time'))
	test_number = models.IntegerField(default=lambda: default_eq('test_number'))
	equipment = models.CharField(max_length=100, default=lambda: default_eq('equip'))
	type_of_wood = models.CharField(max_length=100, choices=wood_types, default=lambda: default_eq('type_of_wood'))
	strength_class = models.CharField(max_length=100, choices=strength_class_types, default=lambda: default_eq('strength_class'))
	glue = models.CharField(max_length=100, default=lambda: default_eq('glue'))
	glue_harderner_amount = models.CharField(max_length=100, blank=True, default=lambda: default_eq('glue_harderner_amount'))
	lamellas_thickness = models.IntegerField(default=lambda: default_eq('lamellas_thickness'))
	lamellas_width = models.IntegerField(default=lambda: default_eq('lamellas_width'))
	lamellas_length = models.IntegerField(default=lambda: default_eq('lamellas_length'))
	fj_length = models.IntegerField(default=lambda: default_eq('fj_length'))
	fj_path = models.IntegerField(default=lambda: default_eq('fj_path'))
	fj_gap = models.IntegerField(default=lambda: default_eq('fj_gap'))
	fj_angle = models.IntegerField(default=lambda: default_eq('fj_angle'))
	fj_orientation = models.CharField(max_length=100, choices=[('Пластевое', 'Пластевое'), ('Ребровое', 'Ребровое')], default=lambda: default_eq('fj_orientation'))
	lamellas_left_moisture = models.IntegerField(default=lambda: default_eq('lamellas_left_moisture'))
	lamellas_right_moisture = models.IntegerField(default=lambda: default_eq('lamellas_right_moisture'))
	glue_pressure = models.FloatField(default=lambda: default_eq('glue_pressure'))
	pressure_time = models.FloatField(blank=True, default=lambda: default_eq('pressure_time'))
	glue_use_amount = models.IntegerField(default=lambda: default_eq('glue_use_amount'))
	glue_batch_number = models.CharField(max_length=100, default=lambda: default_eq('glue_batch_number'))
	glue_expiration_date = models.DateField()
	lamellas_param = models.CharField(max_length=100, default=lambda: default_eq('lamellas_param'))
	lamellas_took_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestLamella_took_person', default=lambda: default_eq('lamellas_took_person'))
	force_crash = models.FloatField()
	time_of_testing = models.IntegerField(blank=True)
	lamellas_strength = models.FloatField()
	passed = models.BooleanField(default=False)
	by_fj_crash = models.IntegerField()
	base_fj_crash = models.IntegerField()
	out_of_fj_crash = models.IntegerField()
	comment = models.TextField(blank=True)
	photo = models.ImageField(upload_to='uploads', blank=True)

	#def save(self):
		#super().save()
		#img = Image.open(self.image.path)
		#if img.height > 600 or img.width > 600:
			#output_size = (600, 600)
			#img.thumbnail(output_size)
			#img.save(self.image.path)

	def __str__(self):
		return (str(self.test_number) + '  Lamellas Test')


class TestDelamination(models.Model):
	test_date = models.DateField()
	test_time = models.TimeField(blank=True, default=None)
	test_number = models.IntegerField()
	equipment = models.CharField(max_length=100)
	type_of_wood = models.CharField(max_length=100, choices=wood_types)
	timber_params = models.CharField(max_length=100)
	sorter_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_sorter_person')
	fj_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_fj_person')
	glue_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_glue_person')
	marking_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestDelamination_marking_person')
	air_moisture = models.IntegerField()
	wood_moisture = models.IntegerField()
	glue_harderner_amount = models.CharField(max_length=100, blank=True)
	glue_temperature = models.IntegerField(blank=True)
	air_temperature = models.IntegerField()
	wood_temperature = models.IntegerField(blank=True)
	glue = models.CharField(max_length=100)
	glue_batch_number = models.CharField(max_length=100)
	glue_expiration_date = models.DateField()
	sample_thickness = models.FloatField()
	sample_width = models.FloatField()
	sample_length = models.FloatField()
	glue_use_amount = models.IntegerField()
	glue_pressure = models.FloatField()
	start_glue_time = models.TimeField(blank=True)
	end_glue_time = models.TimeField(blank=True)
	pressure_time = models.IntegerField(blank=True)
	layer_out_percent = models.IntegerField()
	passed = models.BooleanField(default=False)
	comment = models.TextField(blank=True)
	photo = models.ImageField(upload_to='uploads', blank=True)

	def __str__(self):
		return (str(self.test_number) + '  Delamination Test')


class TestShear(models.Model):
	test_date = models.DateField()
	test_time = models.TimeField(blank=True, default=None)
	test_number = models.IntegerField()
	equipment = models.CharField(max_length=100)
	type_of_wood = models.CharField(max_length=100, choices=wood_types)
	timber_params = models.CharField(max_length=100)
	sorter_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_sorter_person')
	fj_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_fj_person')
	glue_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_glue_person')
	marking_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestShear_marking_person')
	air_moisture = models.IntegerField()
	wood_moisture = models.IntegerField()
	glue_temperature = models.IntegerField(blank=True)
	air_temperature = models.IntegerField()
	wood_temperature = models.IntegerField(blank=True)
	glue = models.CharField(max_length=100)
	glue_batch_number = models.CharField(max_length=100)
	glue_expiration_date = models.DateField()
	sample_thickness = models.FloatField()
	sample_width = models.FloatField()
	sample_length = models.FloatField()
	glue_use_amount = models.IntegerField()
	glue_harderner_amount = models.CharField(max_length=100, blank=True)
	glue_pressure = models.FloatField()
	start_glue_time = models.TimeField(blank=True)
	end_glue_time = models.TimeField(blank=True)
	pressure_time = models.IntegerField(blank=True)
	time_of_testing = models.IntegerField(blank=True)
	layer_ripped_percent1 = models.IntegerField(blank=True)
	layer_ripped_percent2 = models.IntegerField(blank=True)
	layer_ripped_percent3 = models.IntegerField(blank=True)
	layer_ripped_percent4 = models.IntegerField(blank=True)
	layer_ripped_percent5 = models.IntegerField(blank=True)
	layer_ripped_percent_average = models.IntegerField()
	force_crash = models.FloatField()
	passed = models.BooleanField(default=False)
	comment = models.TextField(blank=True)
	photo = models.ImageField(upload_to='uploads', blank=True)

	def __str__(self):
		return (str(self.test_number) + '  Shear Test')


class Nonconformity(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	resp_person = models.ForeignKey(Person, on_delete=models.PROTECT)
	nonconformity_date = models.DateField()

	def __str__(self):
		return self.name

class Tool(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	resp_person = models.ForeignKey(Person, on_delete=models.PROTECT)
	calibration_date = models.DateField()
	next_calibration_date = models.DateField()

	def __str__(self):
		return self.name

glue_expiration_date_1 = default_eq('glue_expiration_date')


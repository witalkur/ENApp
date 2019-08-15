from django.db import models

wood_types = [('spruce', 'spruce'), ('pine', 'pine')]
strength_class_types = [('C14', 'C14'), ('C18', 'C18'), ('C24', 'C24'), ('C30', 'C30')]


class Person(models.Model):
	name = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	training_date = models.DateField()

	def __str__(self):
		return self.name


class TestLamella(models.Model):
	test_date = models.DateField()
	test_number = models.IntegerField()
	equipment = models.CharField(max_length=100)
	type_of_wood = models.CharField(max_length=100, choices=wood_types)
	strength_class = models.CharField(max_length=100, choices=strength_class_types)
	glue = models.CharField(max_length=100)
	lamellas_thickness = models.IntegerField()
	lamellas_width = models.IntegerField()
	lamellas_length = models.IntegerField()
	fj_length = models.IntegerField()
	fj_path = models.IntegerField()
	fj_gap = models.IntegerField()
	fj_angle = models.IntegerField()
	fj_orientation = models.CharField(max_length=100, choices=[('Пластевое', 'Пластевое'), ('Ребровое', 'Ребровое')])
	lamellas_left_moisture = models.IntegerField()
	lamellas_right_moisture = models.IntegerField()
	glue_pressure = models.FloatField()
	pressure_time = models.CharField(max_length=100)
	glue_use_amount = models.IntegerField()
	glue_batch_number = models.CharField(max_length=100)
	glue_expiration_date = models.DateField()
	lamellas_param = models.CharField(max_length=100)
	lamellas_took_person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='TestLamella_took_person')
	force_crash = models.FloatField()
	lamellas_strength = models.FloatField()
	by_fj_crash = models.IntegerField()
	base_fj_crash = models.IntegerField()
	out_of_fj_crash = models.IntegerField()
	comment = models.TextField()
	#photo = models.FileField(upload_to='uploads/')

	def __str__(self):
		return (str(self.test_number) + '  Lamellas Test')


class TestDelamination(models.Model):
	test_date = models.DateField()
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
	glue_temperature = models.IntegerField()
	air_temperature = models.IntegerField()
	wood_temperature = models.IntegerField()
	glue = models.CharField(max_length=100)
	glue_batch_number = models.CharField(max_length=100)
	glue_expiration_date = models.DateField()
	sample_thickness = models.FloatField()
	sample_width = models.FloatField()
	sample_length = models.FloatField()
	glue_use_amount = models.IntegerField()
	glue_pressure = models.FloatField()
	start_glue_time = models.TimeField()
	end_glue_time = models.TimeField()
	pressure_time = models.CharField(max_length=100)
	layer_out_percent = models.IntegerField()
	comment = models.TextField()
	#photo = models.FileField(upload_to='uploads/')

	def __str__(self):
		return (str(self.test_number) + '  Delamination Test')


class TestShear(models.Model):
	test_date = models.DateField()
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
	glue_temperature = models.IntegerField()
	air_temperature = models.IntegerField()
	wood_temperature = models.IntegerField()
	glue = models.CharField(max_length=100)
	glue_batch_number = models.CharField(max_length=100)
	glue_expiration_date = models.DateField()
	sample_thickness = models.FloatField()
	sample_width = models.FloatField()
	sample_length = models.FloatField()
	glue_use_amount = models.IntegerField()
	glue_pressure = models.FloatField()
	start_glue_time = models.TimeField()
	end_glue_time = models.TimeField()
	pressure_time = models.CharField(max_length=100)
	layer_ripped_percent1 = models.IntegerField()
	layer_ripped_percent2 = models.IntegerField()
	layer_ripped_percent3 = models.IntegerField()
	layer_ripped_percent4 = models.IntegerField()
	layer_ripped_percent5 = models.IntegerField()
	layer_ripped_percent_average = models.IntegerField()
	force_crash = models.FloatField()
	comment = models.TextField()
	#photo = models.FileField(upload_to='uploads/')

	def __str__(self):
		return (str(self.test_number) + '  Shear Test')


class Nonconformity(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	resp_person = models.ForeignKey(Person, on_delete=models.PROTECT)
	nonconformity_date = models.DateField()

	def __str__(self):
		return self.name

class Tool(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	resp_person = models.ForeignKey(Person, on_delete=models.PROTECT)
	calibration_date = models.DateField()
	next_calibration_date = models.DateField()

	def __str__(self):
		return self.name
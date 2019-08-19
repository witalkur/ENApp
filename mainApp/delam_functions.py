"""

from .models import TestDelamination
last_delamtests = TestDelamination.objects.all().order_by('-test_date').first()

def def_d_equipment():
	try: return last_delamtests.equipment
	except: return None

def def_d_glue():
	try: return last_delamtests.glue
	except: return None

def def_d_glue_harderner_amount():
	try: return last_bendtests.glue_harderner_amount
	except: return None

def def_d_test_number():
	try: return (int(last_delamtests.test_number) + 1)
	except: return None

def def_d_test_time():
	try: return last_delamtests.test_time
	except: return None

def def_d_type_of_wood():
	try: return last_delamtests.type_of_wood
	except: return None

def def_d_glue_pressure():
	try: return last_delamtests.glue_pressure
	except: return None

def def_d_pressure_time():
	try: return last_delamtests.pressure_time
	except: return None

def def_d_glue_use_amount():
	try: return last_delamtests.glue_use_amount
	except: return None

def def_d_glue_batch_number():
	try: return last_delamtests.glue_batch_number
	except: return None

def def_d_air_moisture():
	try: return last_delamtests.air_moisture
	except: return None

def def_d_timber_params():
	try: return last_delamtests.timber_params
	except: return None

def def_d_sorter_person():
	try: return last_delamtests.sorter_person
	except: return None

def def_d_fj_person():
	try: return last_delamtests.fj_person
	except: return None

def def_d_glue_person():
	try: return last_delamtests.glue_person
	except: return None

def def_d_marking_person():
	try: return last_delamtests.marking_person
	except: return None
	
def def_d_glue_expiration_date():
	try: return last_delamtests.glue_expiration_date
	except: return None

def def_d_wood_moisture():
	try: return last_delamtests.wood_moisture
	except: return None

def def_d_glue_temperature():
	try: return last_delamtests.glue_temperature
	except: return None

def def_d_air_temperature():
	try: return last_delamtests.air_temperature
	except: return None

def def_d_wood_temperature():
	try: return last_delamtests.wood_temperature
	except: return None

	"""
"""

from .models import TestLamella
last_bendtests = TestLamella.objects.all().order_by('-test_date').first()

def def_bt_equipment():
	try: return last_bendtests.equipment
	except: return None

def def_bt_glue():
	try: return last_bendtests.glue
	except: return None

def def_bt_lamellas_thickness():
	try: return last_bendtests.lamellas_thickness
	except: return None

def def_bt_lamellas_width():
	try: return last_bendtests.lamellas_width
	except: return None

def def_bt_lamellas_length():
	try: return last_bendtests.lamellas_length
	except: return None

def def_bt_glue_harderner_amount():
	try: return last_bendtests.glue_harderner_amount
	except: return None

def def_bt_test_number():
	try: return (int(last_bendtests.test_number) + 1)
	except: return None

def def_bt_test_time():
	try: return last_bendtests.test_time
	except: return None

def def_bt_fj_length():
	try: return last_bendtests.fj_length
	except: return None

def def_bt_fj_path():
	try: return last_bendtests.fj_path
	except: return None

def def_bt_fj_gap():
	try: return last_bendtests.fj_gap
	except: return None

def def_bt_fj_angle():
	try: return last_bendtests.fj_angle
	except: return None

def def_bt_type_of_wood():
	try: return last_bendtests.type_of_wood
	except: return None

def def_bt_strength_class():
	try: return last_bendtests.strength_class
	except: return None

def def_bt_fj_orientation():
	try: return last_bendtests.fj_orientation
	except: return None

def def_bt_lamellas_left_moisture():
	try: return last_bendtests.lamellas_left_moisture
	except: return None

def def_bt_lamellas_right_moisture():
	try: return last_bendtests.lamellas_right_moisture
	except: return None

def def_bt_glue_pressure():
	try: return last_bendtests.glue_pressure
	except: return None

def def_bt_pressure_time():
	try: return last_bendtests.pressure_time
	except: return None

def def_bt_glue_use_amount():
	try: return last_bendtests.glue_use_amount
	except: return None

def def_bt_glue_batch_number():
	try: return last_bendtests.glue_batch_number
	except: return None

def def_bt_glue_expiration_date():
	try: return last_bendtests.glue_expiration_date
	except: return None

def def_bt_lamellas_param():
	try: return last_bendtests.lamellas_param
	except: return None

def def_bt_lamellas_took_person():
	try: return last_bendtests.lamellas_took_person
	except: return None

	"""
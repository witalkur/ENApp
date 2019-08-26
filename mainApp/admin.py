from django.contrib import admin
from .models import Person, TestLamella, TestDelamination, TestShear, Nonconformity, Tool, Wood_types, strength_class_types

admin.site.register(Person)
admin.site.register(TestLamella)
admin.site.register(TestDelamination)
admin.site.register(TestShear)
admin.site.register(Nonconformity)
admin.site.register(Tool)
admin.site.register(Wood_types)
admin.site.register(strength_class_types)
from django.contrib import admin
from .models import Person, TestLamella, TestDelamination, TestShear, Nonconformity, Tool

admin.site.register(Person)
admin.site.register(TestLamella)
admin.site.register(TestDelamination)
admin.site.register(TestShear)
admin.site.register(Nonconformity)
admin.site.register(Tool)
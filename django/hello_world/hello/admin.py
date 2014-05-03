from django.contrib import admin
from hello.models import Restaurant, Address, Violation

admin.site.register(Restaurant)
admin.site.register(Address)
admin.site.register(Violation)

from django.contrib import admin

# Register your models here.

from .models import Retailer
from .models import Denomination

admin.site.register(Retailer)
admin.site.register(Denomination)
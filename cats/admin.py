from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Species)
admin.site.register(Description_of_the_cat)
admin.site.register(Photo)
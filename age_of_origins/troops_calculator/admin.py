from django.contrib import admin

# Register your models here.
from .models import Troop, Category

admin.site.register(Troop)
admin.site.register(Category)

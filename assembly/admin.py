from django.contrib import admin

# Register your models here.
from .models import Item, Prep_methods, ItemProfile

admin.site.register(Item)
admin.site.register(Prep_methods)
admin.site.register(ItemProfile)
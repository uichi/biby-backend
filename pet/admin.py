from django.contrib import admin
from .models import CareCategory, Pet, PetCareLog, PetOwnerGroup


admin.site.register(Pet)
admin.site.register(PetOwnerGroup)
admin.site.register(CareCategory)
admin.site.register(PetCareLog)
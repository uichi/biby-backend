from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import Hospital

class HospitalResource(resources.ModelResource):

  class Meta:
    model = Hospital
    fields = ('id', 'name', 'address', 'phone_number', 'support_animal', 'service', )
    import_id_fields = ('id', )

class HospitalAdmin(ImportExportModelAdmin):
  list_display = ('name', 'address', 'phone_number', 'support_animal', 'service', )
  resource_class = HospitalResource

admin.site.register(Hospital, HospitalAdmin)
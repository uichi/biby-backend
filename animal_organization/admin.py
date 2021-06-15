from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


from animal_organization.models import Hospital

class HospitalResource(resources.ModelResource):

  class Meta:
    model = Hospital
    fields = ('id', 'name', 'address', 'phone_number', )
    import_id_fields = ('id', )

class HospitalAdmin(ImportExportModelAdmin):
  list_display = ('name', 'address', 'phone_number', )
  resource_class = HospitalResource

admin.site.register(Hospital, HospitalAdmin)
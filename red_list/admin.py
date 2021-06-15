from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from red_list.models import Category
admin.site.register(Category)

from red_list.models import Classification
admin.site.register(Classification)

from red_list.models import Animal

class AnimalResource(resources.ModelResource):

  category = Field(attribute='category', column_name='category', widget=ForeignKeyWidget(Category, 'name'))
  classification = Field(attribute='classification', column_name='classification', widget=ForeignKeyWidget(Classification, 'name'))

  class Meta:
    model = Animal
    fields = ('id', 'japanese_name', 'scientific_name', 'category', 'classification', )
    import_id_fields = ('id', )

class AnimalAdmin(ImportExportModelAdmin):
  list_display = ('japanese_name', 'scientific_name','category', 'classification', )
  resource_class = AnimalResource

admin.site.register(Animal, AnimalAdmin)
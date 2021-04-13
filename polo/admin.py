from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import PoloBrand , Polo_Id , Reverse_check

@admin.register(PoloBrand,Polo_Id , Reverse_check)
class PersonAdmin(ImportExportModelAdmin):
    pass





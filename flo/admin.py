from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Flo_Brand , Flo_Id , Reverse_check

@admin.register(Flo_Brand,Flo_Id , Reverse_check)
class PersonAdmin(ImportExportModelAdmin):
    pass


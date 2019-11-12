from django.contrib import admin
from . import models
from swengs.homework.models import OEM, CPU


class CPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'coremultiplier', 'release_date', 'price', 'manufacturer')
    search_fields = ('name', 'coremultiplier')
    sortable_by = 'price'
    list_filter = ['manufacturer']


admin.site.register(CPU, CPUAdmin)


class OEMAdmin(admin.ModelAdmin):
    pass


admin.site.register(OEM, OEMAdmin)

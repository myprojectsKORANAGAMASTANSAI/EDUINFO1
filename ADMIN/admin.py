from django.contrib import admin
from .models import Admission,CustomUser
# Register your models here.

class kk(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Admission)


admin.site.register(CustomUser)
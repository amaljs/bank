from django.contrib import admin
from .models import Branches,City,Task
# Register your models here.
class AdminBranch(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Branches,AdminBranch)

class AdminCity(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City,AdminCity)



class AdminTask(admin.ModelAdmin):
    list_display = ['name','age','mailid','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Task,AdminTask)
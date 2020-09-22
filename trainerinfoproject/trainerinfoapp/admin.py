from django.contrib import admin
from .models import TrainerInfo

# Register your models here.
class TrainerInfoAdmin(admin.ModelAdmin):
    '''
        Admin View for TrainerInfo
    '''
    list_display = ('FIRST_NAME','LAST_NAME','DOMAIN','EXPERIENCE','BRANCH','ADDRESS','GENDER','SALARY')

admin.site.register(TrainerInfo, TrainerInfoAdmin)
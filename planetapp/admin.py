from django.contrib import admin
from .models import PlanetModel,InformationModel,ContactInfoModel,User

# Register your models here.
admin.site.register(PlanetModel)
admin.site.register(InformationModel)
admin.site.register(ContactInfoModel)


admin.site.register(User)



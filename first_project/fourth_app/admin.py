from django.contrib import admin
from fourth_app.models import AccessRecord, Webpage, Topic

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# Register your models here.

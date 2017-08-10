from django.contrib import admin
from main.models import MyModel, TestModel, NameModel, VogabyggdModel

# Register your models here.

admin.site.register(MyModel)
admin.site.register(TestModel)
admin.site.register(NameModel)
admin.site.register(VogabyggdModel)

from django.contrib import admin
from main.models import MyModel, TestModel, NameModel

# Register your models here.

admin.site.register(MyModel)
admin.site.register(TestModel)
admin.site.register(NameModel)

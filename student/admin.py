from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Parent)
admin.site.register(Account)
admin.site.register(Token)
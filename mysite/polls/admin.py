from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# To show tables for interact add/change/delete more easily
admin.site.register(Question)
admin.site.register(Choice)


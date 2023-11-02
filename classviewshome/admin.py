from django.contrib import admin
from .models import *

admin.site.register(Article)
# Register your models here.
admin.site.register(Book)
admin.site.register(CustomUser)
# -*- coding:utf-8 -*-

from django.contrib import admin
from vote.models import *

# class ShowAdmin(admin.ModelAdmin):


# class VotesAdmin(admin.ModelAdmin):	


admin.site.register(Show)
admin.site.register(Votes)
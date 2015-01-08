# -*- coding:utf-8 -*-

from django.contrib import admin
from vote.models import *

class VotesAdmin(admin.ModelAdmin):	
	date_hierarchy = 'datetime_voted'
	list_display = ('name','department','show','datetime_voted')
	list_filter = ('department',)

class VoteInline(admin.StackedInline):
	model = Votes
	extra = 1 

class ShowAdmin(admin.ModelAdmin):
	inlines = [VoteInline,]
	list_display = ('name','department','year','get_votes_count')
	list_filter = ('department','year')

admin.site.register(Show,ShowAdmin)
admin.site.register(Votes,VotesAdmin)
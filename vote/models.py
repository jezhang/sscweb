# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
import logging,datetime
from uuid import uuid4


DEPARTMENTS = (
	('1',u'eBusiness'),	
	('2',u'PMO'),
	('3',u'HR'),
	('4',u'Infra'),
	('5',u'Finance'),
	('6',u'BI'),
	('7',u'C&BI'),
	('8',u'Transportation'),
	('9',u'DBA'),
)

class Show(models.Model):
	uid = models.CharField(max_length=50,unique=True,verbose_name='UUID',default=uuid4().hex)
	name = models.CharField(max_length=100,verbose_name='Name')
	year = models.CharField(max_length=4,verbose_name='Year')
	department = models.CharField(max_length=1,verbose_name='department',choices=DEPARTMENTS)

	class Meta:
		verbose_name = u'节目show'
		verbose_name_plural = u'节目show'

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.uid = uuid4().hex
		return super(Show, self).save(*args, **kwargs)

	def get_votes_count(self):
		return self.votes_set.filter(show=self).count()
	# get_votes_count.admin_order_field = 
	get_votes_count.short_description = '票数统计'

class Votes(models.Model):
	datetime_voted = models.DateTimeField(auto_now_add=True,verbose_name='投票时间')
	name = models.CharField(max_length=50,blank=True,null=True,verbose_name='姓名')
	department = models.CharField(max_length=2,blank=True,null=True,verbose_name='部门',choices=DEPARTMENTS)
	# email = models.EmailField(max_length=50,blank=True,null=True,verbose_name='电子邮件')
	show = models.ForeignKey(Show,blank=True,null=True,verbose_name='节目名称')

	class Meta:
		verbose_name = u'节目投票'
		verbose_name_plural = u'节目投票'

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.datetime_voted = datetime.datetime.today()
		return super(Votes, self).save(*args, **kwargs)		
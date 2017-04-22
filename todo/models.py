
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    tid = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User)
    todo = models.CharField(max_length=50)
    flag = models.CharField(max_length=2, default='1')
    priority = models.CharField(max_length=2,default='3')
    # pubtime = models.DateTimeField(auto_now_add=True)无法修改
    pubtime = models.DateTimeField('保存日期',default = timezone.now)
    lastdate = models.DateTimeField('最后修改日期', auto_now = True)

    def __str__(self):
        return u'%d %s %s' % (self.tid, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']


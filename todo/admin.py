
from __future__ import unicode_literals

from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['todo']}),
        ('Priority', {'fields': ['priority']}),
        ('pubtime', {'fields': ['pubtime']}),
        # ('user', {'fields': ['user']}),
        ('flag', {'fields': ['flag']}),
    ]
    list_display = ('todo','tid',  'priority', 'flag', 'pubtime','lastdate')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)


admin.site.register(Todo, TodoAdmin)

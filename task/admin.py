from django.contrib import admin
from .models import Task, State


class TaskAdmin(admin.ModelAdmin):  # add this
      list_display = ('title', 'description', 'state') # add this

class StateAdmin(admin.ModelAdmin):  # add this
      model = State
      extra = 3

# Register your models here.
admin.site.register(Task, TaskAdmin) # add this
admin.site.register(State,StateAdmin) # add this
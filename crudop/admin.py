from django.contrib import admin
from .models import Tasklist

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    model = Tasklist
    list_display = ["id", "user", "title", "created_on", "updated_on"]


admin.site.register(Tasklist, TaskAdmin)

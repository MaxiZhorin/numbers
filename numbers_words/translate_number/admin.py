from django.contrib import admin
from .models import Number_word




class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Number_word._meta.fields]

    class Meta:
        model = Number_word


admin.site.register(Number_word, StatusAdmin)

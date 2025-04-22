from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Calculator

@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display = ('amount', 'from_currency', 'to_currency', 'result', 'date_converted')
    search_fields = ('from_currency', 'to_currency')
    list_filter = ('from_currency', 'to_currency', 'date_converted')

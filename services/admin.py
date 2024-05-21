from django.contrib import admin
from .models import Services

# Register your models here.
@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
  readonly_fields = ("created", "updated")
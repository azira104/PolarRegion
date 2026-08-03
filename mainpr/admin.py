from django.contrib import admin

from .models import VisitorLog


@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('visitor_key', 'page_path', 'device_type', 'country', 'traffic_source', 'accessed_at')
    list_filter = ('device_type', 'country', 'traffic_source', 'accessed_at')
    search_fields = ('visitor_key', 'page_path', 'country', 'traffic_source', 'ip_address')
    ordering = ('-accessed_at',)

from django.db import models


class VisitorLog(models.Model):
    visitor_key = models.CharField(max_length=100, db_index=True)
    ip_address = models.CharField(max_length=64, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    device_type = models.CharField(max_length=30, default='desktop')
    country = models.CharField(max_length=80, default='Unknown')
    page_path = models.CharField(max_length=255, default='/')
    traffic_source = models.CharField(max_length=255, default='direct')
    accessed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-accessed_at']

    def __str__(self):
        return f"{self.visitor_key} - {self.page_path}"


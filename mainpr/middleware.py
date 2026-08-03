import re
import uuid
from datetime import datetime

from django.utils import timezone

from .models import VisitorLog


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith('/admin/') or request.path.startswith('/static/'):
            return response

        try:
            visitor_key = request.session.get('analytics_uid')
            if not visitor_key:
                visitor_key = uuid.uuid4().hex
                request.session['analytics_uid'] = visitor_key

            user_agent = request.META.get('HTTP_USER_AGENT', '')
            device_type = 'desktop'
            if 'mobile' in user_agent.lower():
                device_type = 'mobile'
            elif 'tablet' in user_agent.lower():
                device_type = 'tablet'

            traffic_source = request.META.get('HTTP_REFERER') or 'direct'
            referrer_domain = 'direct'
            if traffic_source and traffic_source != 'direct':
                referrer_domain = traffic_source.split('/')[2] if '//' in traffic_source else traffic_source

            country = request.META.get('HTTP_CF_IPCOUNTRY') or 'Unknown'
            ip_address = request.META.get('REMOTE_ADDR', 'unknown')

            VisitorLog.objects.create(
                visitor_key=visitor_key,
                ip_address=ip_address,
                user_agent=user_agent,
                device_type=device_type,
                country=country,
                page_path=request.path,
                traffic_source=referrer_domain,
                accessed_at=timezone.now(),
            )
        except Exception:
            # Keep the site running even if analytics storage is not yet migrated.
            pass

        return response

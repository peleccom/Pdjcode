#!/usr/bin/env python
try:
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'pastebin.settings'
    from django.utils import timezone
    from django.conf import settings
    from pastebinapp.models import Paste

    today = timezone.now()
    cutoff = (today - timezone.timedelta(days=settings.EXPIRY_DAYS))
    print(cutoff)
    Paste.objects.filter(timestamp__lt=cutoff).delete()
except Exception,e:
    print e

raw_input()

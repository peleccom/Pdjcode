#!/usr/bin/env python
try:
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'pastebin.settings'
    import datetime
    from django.conf import settings
    from pastebinapp.models import Paste

    today = datetime.date.today()
    cutoff = (today - datetime.timedelta(days=settings.EXPIRY_DAYS))
    Paste.objects.filter(timestamp__lt=cutoff).delete()
except Exception,e:
    print e

input()

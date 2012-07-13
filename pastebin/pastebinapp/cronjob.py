#!/usr/bin/env python
import datetime
from django.conf import settings
from pastesbin.pastebinapp.models import Paste

today = datetime.date.today()
cutoff = (today - datetime.timedelta(days=settings.EXPIRY_DAYS))
Paste.objects.filter(timestamp__lt=cutoff).delete()

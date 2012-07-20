import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = "pastebin.settings"
from django.conf import settings

def vacuum_db():
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('VACUUM')
    connection.close()

if __name__== "__main__":
    print "Vacuum database..."
    before = os.stat(settings.DATABASES['default']['NAME']).st_size
    print "Size before: %s bytes" % before
    vacuum_db()
    after =os.stat(settings.DATABASES['default']['NAME']).st_size
    print "Size after: %s bytes" % after
    print "Reclaimed: %s bytes" % (before-after)
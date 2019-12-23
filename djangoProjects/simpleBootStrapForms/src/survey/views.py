"""
This module contains all the views for this application
"""
import datetime
import random

from django.http import HttpResponse

def forms_view(request):
    """This is the view that would randomly return different survey forms
    it is based on random number generator
    """
    form_no = random.randint(0, 5)
    form_codes = [
        '1FAIpQLSdPT97YlqNhkPtca3BTsLUFnIsLZmFKG-TfVs67DKvqCYXVWA',
        '1FAIpQLSc_sq8vhuGqHS1PQt7xA9Vl6xacKpMXs9qtZIt4ecuK9eNkKQ',
        '1FAIpQLSdPT97YlqNhkPtca3BTsLUFnIsLZmFKG-TfVs67DKvqCYXVWA',
        '1FAIpQLSc_sq8vhuGqHS1PQt7xA9Vl6xacKpMXs9qtZIt4ecuK9eNkKQ',
        '1FAIpQLSdPT97YlqNhkPtca3BTsLUFnIsLZmFKG-TfVs67DKvqCYXVWA',
        '1FAIpQLSc_sq8vhuGqHS1PQt7xA9Vl6xacKpMXs9qtZIt4ecuK9eNkKQ',
    ]
    embed_html = '''<iframe
    src="https://docs.google.com/forms/d/e/%s/viewform?embedded=true"
    width="1024" height="1024" frameborder="0" marginheight="0"
    marginwidth="0">Loading…</iframe>''' % form_codes[form_no]
    now = datetime.datetime.now()
    html = "<html><body>is now %s and random Integer is %s.</body></html>" % (now, str(form_no))
    html = "<html><body>%s</body></html>" % (embed_html)
    return HttpResponse(html)

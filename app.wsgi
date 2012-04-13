import os
import sys
import site
# use the virtualenv's packages
site.addsitedir( os.path.abspath(os.path.join(os.path.dirname(__file__), "../env/lib/python2.6/site-packages")))
# put the Django project on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ["DJANGO_SETTINGS_MODULE"] = "newrelicdemo.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import newrelic.agent
newrelic.agent.initialize('../newrelic.ini')
                                                                               
application = newrelic.agent.wsgi_application()(application)

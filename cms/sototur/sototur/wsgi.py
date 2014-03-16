import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/sototur/cms/sototur_virt/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/sototur/cms/sototur')
sys.path.append('/home/sototur/cms/sototur/sototur')

os.environ['DJANGO_SETTINGS_MODULE'] = 'sototur.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/sototur/cms/sototur_virt/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

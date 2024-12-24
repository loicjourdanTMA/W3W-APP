import os
import sys

# Path to your project directory
project_home = '/home/LoicJourdan/W3W-APP'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Path to the virtual environment
activate_this = '/home/LoicJourdan/.virtualenvs/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'W3W-APP.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

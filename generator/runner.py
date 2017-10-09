import sys
import os
import time
from django.core.wsgi import get_wsgi_application

"""
let you run standalone scripts that import django library
example :
       python runner.py adsapi.recbyrelfb.poller
  or   python runner.py adsapi/recbyrelfb/poller
  or   python runner.py adsapi\recbyrelfb\poller.py
"""
def run(argv):
    if len(argv) < 2:
        print "Usage : python runner.py module_name"
        sys.exit(2)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = "settings"
    application = get_wsgi_application()
    os.environ['PYTHONPATH'] = "."
    
    module = argv[1]
    module = module.replace("\\",".").replace("/",".") #accept parent\child\child... form
    if module.endswith(".py") :
        module = module[:-3]
    exec("from %s import main" % module)
    main(argv[1:])

if __name__ == "__main__":
    	run(sys.argv)

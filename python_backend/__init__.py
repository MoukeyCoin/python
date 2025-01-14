from .settings import *
import os
import django


# """Run administrative tasks."""
# if os.environ.get('DJANGO_ENV') == 'production':
#     from .settings.production import * # type: ignore
# elif os.environ.get('DJANGO_ENV') == 'development':
#     from .settings.development import * # type: ignore
# else:
#     from .settings.development import * # type: ignore
   
django.setup()
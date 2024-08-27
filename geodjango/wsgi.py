"""
WSGI config for geodjango project.

Exposes the WSGI callable as a module-level variable named `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

# Configura o ambiente Django para usar as configurações do projeto 'geodjango'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodjango.settings')

# Obtém a aplicação WSGI do Django
application = get_wsgi_application()

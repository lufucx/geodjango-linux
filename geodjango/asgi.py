"""
ASGI config for geodjango project.

Exposes the ASGI callable as a module-level variable named `application`.
"""

import os
from django.core.asgi import get_asgi_application

# Configura o ambiente Django para usar as configurações do projeto 'geodjango'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodjango.settings')

# Obtém a aplicação ASGI do Django
application = get_asgi_application()

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'markers': reverse('marker-list', request=request, format=format),  # Use 'marker-list' instead of 'markers-list'
        'posts': reverse('post-list', request=request, format=format)
    })

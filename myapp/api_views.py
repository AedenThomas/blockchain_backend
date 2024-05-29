from rest_framework import viewsets
from .models import EncryptedContent
from .serializers import EncryptedContentSerializer

class EncryptedContentViewSet(viewsets.ModelViewSet):
    queryset = EncryptedContent.objects.all()
    serializer_class = EncryptedContentSerializer
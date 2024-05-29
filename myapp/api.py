# /Users/aeden/Developer/cryptovault/blockchain_backend/myapp/api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import encrypt_content

@api_view(['POST'])
def encrypt_api(request):
    content = request.data.get('content')
    encrypted_content, key = encrypt_content(content)
    return Response({'encrypted_content': encrypted_content.decode('utf-8'), 'key': key.decode('utf-8')}) 
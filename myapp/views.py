# myapp/views.py
from django.urls import path
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EncryptedContent
from .serializers import EncryptedContentSerializer
from .utils import encrypt_content, upload_to_storage, decrypt_content, retrieve_from_pinata
from web3 import Web3
import uuid
from django.http import HttpResponse
import binascii
from cryptography.fernet import Fernet, InvalidToken
import base64





def generate_unique_identifier():
    return str(uuid.uuid4())


# @api_view(['POST'])
# def create_encrypted_content(request):
#     content = request.data.get('content')
#     encrypted_content, key = encrypt_content(content)
#     content_hash = upload_to_storage(encrypted_content)
#     unique_identifier = generate_unique_identifier()

#     encrypted_content_obj = EncryptedContent.objects.create(
#         content_hash=content_hash,
#         unique_identifier=unique_identifier,
#         key=key.decode('utf-8') if key else None
#     )

#     serializer = EncryptedContentSerializer(encrypted_content_obj)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_encrypted_content(request):
    content = request.data.get('content')
    encrypted_content, key = encrypt_content(content)
    content_hash = upload_to_storage(encrypted_content)
    unique_identifier = generate_unique_identifier()

    encrypted_content_obj = EncryptedContent.objects.create(
        content_hash=content_hash,
        unique_identifier=unique_identifier,
    )

    serializer = EncryptedContentSerializer(encrypted_content_obj)
    return Response({'content_hash': content_hash, 'unique_identifier': unique_identifier, 'key': key.decode('utf-8')})

urlpatterns = [
    path('api/create-encrypted-content/', create_encrypted_content,
         name='create_encrypted_content'),
    # other URL patterns...
]

def retrieve_encrypted_content(request, unique_identifier):
    try:
        encrypted_content_obj = EncryptedContent.objects.get(unique_identifier=unique_identifier)
        content_hash = encrypted_content_obj.content_hash

        try:
            encrypted_content = retrieve_from_pinata(content_hash)
        except requests.exceptions.ConnectionError:
            return HttpResponse('Failed to retrieve encrypted content. Please check your network connection.', status=500)

        user_provided_key = request.GET.get('encryptionKey', None)
        if user_provided_key:
            # Validate the user-provided key format
            # ...

            key = user_provided_key.encode('utf-8')
            decrypted_content = decrypt_content(encrypted_content, key)
            return HttpResponse(decrypted_content, content_type='text/plain')
        else:
            return HttpResponse('Encryption key is required.', status=400)
    except EncryptedContent.DoesNotExist:
        return HttpResponse('Encrypted content not found', status=404)
    except (InvalidToken, ValueError):
        return HttpResponse('Invalid encryption key provided.', status=400)
        
# def retrieve_encrypted_content(request, unique_identifier):
#     try:
#         encrypted_content_obj = EncryptedContent.objects.get(unique_identifier=unique_identifier)
#         content_hash = encrypted_content_obj.content_hash

#         # Initially set key to None or fetch from your model if needed
#         key = None

#         user_provided_key = request.GET.get('encryptionKey', None)
#         if user_provided_key:
#             # Validate the user-provided key for correct length and format
#             if len(user_provided_key) != 44:  # Fernet keys are 44 characters long, including padding
#                 return HttpResponse('Invalid encryption key format.', status=400)
#             try:
#                 # Decode the key to check if it's valid base64
#                 key_bytes = base64.urlsafe_b64decode(user_provided_key)
#                 # Verify the decoded key is 32 bytes long, which is required for a Fernet key
#                 if len(key_bytes) != 32:
#                     return HttpResponse('Invalid encryption key.', status=400)
#                 key = user_provided_key.encode('utf-8')
#             except (ValueError, binascii.Error):
#                 return HttpResponse('Invalid encryption key format.', status=400)

#         try:
#             encrypted_content = retrieve_from_pinata(content_hash)
#         except requests.exceptions.ConnectionError:
#             return HttpResponse('Failed to retrieve encrypted content. Please check your network connection.', status=500)

#         decrypted_content = decrypt_content(encrypted_content, key)
#         return HttpResponse(decrypted_content, content_type='text/plain')
#     except EncryptedContent.DoesNotExist:
#         return HttpResponse('Encrypted content not found', status=404)
#     except (InvalidToken, ValueError):
#         return HttpResponse('Invalid encryption key provided.', status=400)

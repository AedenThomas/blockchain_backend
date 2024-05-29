# /Users/aeden/Developer/cryptovault/blockchain_backend/myapp/models.py
from django.db import models

# class EncryptedContent(models.Model):
#     content_hash = models.CharField(max_length=100)
#     unique_identifier = models.CharField(max_length=100, unique=True)
#     key = models.CharField(max_length=100, null=True, blank=True) 
#     created_at = models.DateTimeField(auto_now_add=True)

class EncryptedContent(models.Model):
    content_hash = models.CharField(max_length=255)
    unique_identifier = models.CharField(max_length=255, unique=True)
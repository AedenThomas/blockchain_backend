from rest_framework import serializers
from .models import EncryptedContent

# class EncryptedContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EncryptedContent
#         fields = '__all__'

class EncryptedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncryptedContent
        fields = ['content_hash', 'unique_identifier']
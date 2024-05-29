# myapp/utils.py
import os
from cryptography.fernet import Fernet
import ipfshttpclient
from .pinata import upload_to_pinata
import requests
import json

# Encryption
def encrypt_content(content):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    if isinstance(content, dict):
        content_to_encrypt = json.dumps(content)  # Convert dict to JSON string
    else:
        content_to_encrypt = content  # Assume content is already a suitable format (e.g., string)
    encrypted_content = cipher.encrypt(content_to_encrypt.encode())
    return encrypted_content, key  # Return key as bytes


def upload_to_storage(encrypted_content):
    content_hash = upload_to_pinata(encrypted_content)
    return content_hash

def retrieve_from_pinata(content_hash):
    # Make a request to Pinata to retrieve the encrypted content
    pinata_gateway_url = f'https://gateway.pinata.cloud/ipfs/{content_hash}'
    response = requests.get(pinata_gateway_url)
    response.raise_for_status()
    return response.content

    
def decrypt_content(encrypted_content, key):
    cipher = Fernet(key)
    decrypted_content = cipher.decrypt(encrypted_content)
    return decrypted_content.decode() 
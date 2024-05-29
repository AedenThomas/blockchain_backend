import os
import requests

PINATA_API_URL = 'https://api.pinata.cloud/pinning/pinFileToIPFS'

headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIwOGE0YWRlNy0zNTdmLTQ0MDUtYTFiMi1iOWY4MGFlYjM5ZmYiLCJlbWFpbCI6InBpbmF0YS5yZXNvcnQ1OTVAc2ltcGxlbG9naW4uY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9LHsiaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImMzMTE0ZTdkZDJiOTdkMzUyNjgxIiwic2NvcGVkS2V5U2VjcmV0IjoiMDQxYjhjMzJmNmEzMmRjYzQ1MDA1OWYzOGZjNzU0YjBiYjkyYjM3YTU3YmE4OTZlYmMzNjgwM2UzZDdjMjlhOCIsImlhdCI6MTcxMjIxNjIyOH0.qMKaawPAgrWOmQ9xPIgigevQhZHKXuEZbCVpsKTTtSM"
    }


def upload_to_pinata(encrypted_content):
    files = {
        'file': ('encrypted_content.txt', encrypted_content)
    }
    response = requests.post(PINATA_API_URL, files=files, headers=headers)
    response.raise_for_status()
    return response.json()['IpfsHash']
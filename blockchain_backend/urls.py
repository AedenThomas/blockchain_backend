# blockchain_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.api_views import EncryptedContentViewSet
from myapp.views import create_encrypted_content, retrieve_encrypted_content
from myapp.api import encrypt_api

router = routers.DefaultRouter()
router.register(r'encrypted-content', EncryptedContentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/encrypt/', encrypt_api, name='encrypt_api'),

    path('api/create-encrypted-content/', create_encrypted_content,
         name='create_encrypted_content'),
    path('api/retrieve-content/<str:unique_identifier>/',
         retrieve_encrypted_content, name='retrieve_encrypted_content'),
    # other URL patterns...
]

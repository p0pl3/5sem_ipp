from django.urls import path, include
from rest_framework import routers

from contacts.views import ContactModelViewSet

router = routers.DefaultRouter()
router.register(r'contact', ContactModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

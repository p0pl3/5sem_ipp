from rest_framework.viewsets import ModelViewSet

from contacts.models import Contact
from contacts.serializer import ContactSerializer


class ContactModelViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

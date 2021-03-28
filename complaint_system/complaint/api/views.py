import logging
from django.http import Http404
from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ComplaintSerializer
from complaint.models import Complaint


logger = logging.getLogger(__name__)


class ListCreatComplaintView(generics.ListCreateAPIView) :
    permission_classes= (IsAuthenticated ,)
    serializer_class = ComplaintSerializer

    def get_queryset(self) :
        return Complaint.objects.all()    


class SingleComplaintView(generics.RetrieveUpdateDestroyAPIView) :
    permission_classes = (IsAuthenticated ,)
    serializer_class = ComplaintSerializer

    def get_object(self):
        id = self.kwargs.get('id')
        try:
            return Complaint.objects.get(id=id)
        except Complaint.DoesNotExist:
            logger.error('Copmlaint does not exist')
            raise Http404   
    
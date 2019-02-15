from rest_framework import generics,status
from rest_framework.response import Response

from .decorators import validate_request_data
from .models import FsInstitutionNotification, FsInstitution
from .serializers import NotificationSerializer, InstitutionSerializer


class NotificationList(generics.ListCreateAPIView):
    queryset = FsInstitutionNotification.objects.all()
    serializer_class = NotificationSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        institution_id = request.data["institution"]
        institution_obj = FsInstitution.objects.get(id=institution_id)
        a_notification = FsInstitutionNotification.objects.create(
            title=request.data["title"],
            institution=institution_obj
        )
        return Response(
            data=NotificationSerializer(a_notification).data,
            status=status.HTTP_201_CREATED
        )


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FsInstitutionNotification.objects.all()
    serializer_class = NotificationSerializer

class InstitutionList(generics.ListCreateAPIView):
    queryset = FsInstitution.objects.all()
    serializer_class = InstitutionSerializer    
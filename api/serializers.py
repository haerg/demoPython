from rest_framework import serializers
from . import models

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = models.FsInstitution

class NotificationSerializer(serializers.ModelSerializer):
	institution = InstitutionSerializer(read_only=True)
	class Meta:
		fields = ('id', 'title', 'institution')
		model = models.FsInstitutionNotification
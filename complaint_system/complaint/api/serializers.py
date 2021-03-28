from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from complaint.models import Complaint

class ComplaintSerializer(serializers.ModelSerializer) :
    image = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['png','jpg', 'jpeg'])])

    class Meta :
        model = Complaint
        fields = ('title', 'description','image')
    

#serializer
from rest_framework import serializers

from anything.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields ='__all__'
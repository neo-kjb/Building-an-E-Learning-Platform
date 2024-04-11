from rest_framework import serializers
from courses.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fileds = ["id", "title", "slug"]

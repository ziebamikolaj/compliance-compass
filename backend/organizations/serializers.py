from rest_framework import serializers

from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ["id", "name", "description", "location", "date_created"]
        read_only_fields = ["date_created"]

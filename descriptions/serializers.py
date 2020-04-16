from rest_framework import serializers
from .models import DescriptionComparision


class DescriptionPostSerializer(serializers.ModelSerializer):
    """ Compares likeness of two given incident descriptions."""
    first_description = serializers.CharField(required=True)
    second_description = serializers.CharField(required=True)

    class Meta:
        model = DescriptionComparision
        fields = ('first_description','second_description')

    def validate(self, attrs):
        first_description = attrs.get('first_description',None)
        second_description = attrs.get('second_description',None)

        #VALIDATION
        if first_description is None:
            raise serializers.ValidationError(
                'First Description is missing.'
            )

        if second_description is None:
            raise serializers.ValidationError(
                'Second Description is missing.'
            )

        return attrs




from rest_framework import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    def validate_age(self, value):
        if value < 1 or value > 50:
            raise serializers.ValidationError(
                "Age must be between 1 and 50."
            )
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError(
                "Enter a valid email address."
            )
        return value

    def validate_name(self, value):
        return value.strip()

        if " " in value:
            raise serializers.ValidationError(
                "Name must not contain spaces."
            )

        return value

    class Meta:
        model = Student
        fields = '__all__'

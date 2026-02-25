from rest_framework import serializers
from .models import Book
import datetime

class BookSerializer(serializers.ModelSerializer):

    # Validation for year
    def validate_published_date(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'
from rest_framework import serializers
from .models import Book
import datetime

class BookSerializer(serializers.ModelSerializer):

    # Validation for year
    def validate_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'
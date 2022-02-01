from rest_framework import serializers 
from myapp.models import Movie

class MovieSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Movie
        fields = (
            'id',
            'name',
            'description',
            'release_date'
        )
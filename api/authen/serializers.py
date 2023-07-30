from rest_framework import serializers
# from rest_framework import 
from . models import data

class dataSerializer(serializers.ModelSerializer):

    class Meta:
        model = data
        fields = '__all__'
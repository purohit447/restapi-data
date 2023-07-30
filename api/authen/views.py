from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import data
from . serializers import dataSerializer

class dataList(APIView):
    def get(self, request, user_id = None):
        if user_id is None:
            getquery = data.objects.all();
        else:
            getquery = data.objects.filter(user_id=user_id)
        serializer = dataSerializer(getquery, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = dataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        # Get the data object based on the user_id
        data_object = get_object_or_404(data, user_id=user_id)

        # Update the data object with the new data from the request
        serializer = dataSerializer(data_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        # Get the data object based on the user_id
        data_object = get_object_or_404(data, user_id=user_id)

        # Delete the data object
        data_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
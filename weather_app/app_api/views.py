from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import render, get_object_or_404
# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by city': '/?city=city',
        'Search by timstamp': '/?date=timestamp',
       
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)
@api_view(['POST'])
def add_items(request):
    item = WeatherDataSerializer(data=request.data)
 
    # validating for already existing data
    if WeatherData.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)   
@api_view(['GET'])
def view_items(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = WeatherData.objects.filter(**request.query_params.dict())
    else:
        items = WeatherData.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = WeatherDataSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def update_items(request, pk):
    item = WeatherData.objects.get(pk=pk)
    data = WeatherDataSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(WeatherData, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)         
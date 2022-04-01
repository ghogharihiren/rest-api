from urllib.request import Request
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import * 


# Create your views here.

@api_view(['GET'])
def index(request):
    api_urls = {
        'index':'/',
        'all-data':'/all-data/',
        'one-data':'/one-data/id',
        'create-data':'/create-data/',
        'update-data':'/update-data/id',
        'delete-data':'/delete-data/id',
    }
    return Response(api_urls)
@api_view(['GET'])
def all_data(request):
    uid=user.objects.all()
    serializer =userSerializer(uid,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def one_data(request,pk):
    uid=user.objects.get(id=pk)
    serializer =userSerializer(uid)
    return Response(serializer.data)

@api_view(['GET','POST'])
def create_data(request):
    if request.method == 'POST':
        serializer =userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
   
    data = {
        "id": 'id',
        "task": "Task Title",
        "details": "Details of task",
        "status": 'true or false'
    }
    return Response(data)

@api_view(['GET','PUT'])
def update_data(request,pk):
    uid=user.objects.get(id=pk)
    if request.method == 'PUT':
        serializer=userSerializer(uid,data=request.data)
        if serializer.is_valid():
                serializer.save()
        return Response(serializer.data) 
    serializer=userSerializer(uid)
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def delete_data(request,pk):
    if request.method == 'DELETE':
        try:
            uid=user.objects.get(id=pk)
            uid.delete()
            return Response("delete data")
        except:
            return Response('Invalid Id')
    else:
        try:

            uid = user.objects.get(id=pk)
            serializer = userSerializer(uid)
            return Response(serializer.data)
        except:
            return Response('Data not found')    
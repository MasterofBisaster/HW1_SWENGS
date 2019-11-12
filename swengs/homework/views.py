from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from swengs.homework.models import OEM
from swengs.homework.serializers import OEMSerializer


@api_view(['GET', 'POST'])
def oem_list(request):
    if request.method == "GET":
        oems = OEM.objects.all()
        serializer = OEMSerializer(oems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OEMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def oem_detail(request, pk):

    try:
        oem = OEM.objects.get(pk=pk)
    except OEM.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OEMSerializer(oem)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OEMSerializer(oem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        oem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
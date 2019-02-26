from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from salah.serializer import Departserializer ,Productsserializer ,Imagesserializer
from rest_framework.decorators import api_view
from rest_framework import status
from salah.models import Depart , Products,Images

# Create your views here.


@api_view(['GET','POST'])
def Departserializers(requset):
    if requset.method == 'POST':
        serializer = Departserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    if requset.method == 'GET':
        depart = Depart.objects.all()
        serializer = Departserializer(depart,many=True)
        return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def Departserializersd(requset, pk):
    try:
        depart = Depart.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(depart)


    if requset.method == 'GET':
        serializer = Departserializer(depart)
        return Response(serializer.data)


    if requset.method == 'PUT':
        serializer = Departserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_201_CREATED)


    if requset.method == 'DELETE':
        depart.delete()
        departS = Depart.objects.all()
        serializer = Departserializer(departS,many=True)
        return Response(serializer.data)



@api_view(['GET','POST'])
def Productsserializers(requset):
    if requset.method == 'POST':
        serializer = Productsserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    if requset.method == 'GET':
        depart = Products.objects.all()
        serializer = Productsserializer(depart,many=True)
        return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def Productsserializerd(requset, pk):
    try:
        depart = Products.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(depart)


    if requset.method == 'GET':
        serializer = Productsserializer(depart)
        return Response(serializer.data)


    if requset.method == 'PUT':
        serializer = Productsserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_201_CREATED)


    if requset.method == 'DELETE':
        depart.delete()
        departS = Products.objects.all()
        serializer = Productsserializer(departS,many=True)
        return Response(serializer.data)



@api_view(['GET','POST'])
def ImagesserializerS(requset):
    if requset.method == 'POST':
        serializer = Imagesserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    if requset.method == 'GET':
        depart = Images.objects.all()
        serializer = Imagesserializer(depart,many=True)
        return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def ImagesserializerD(requset, pk):
    try:
        depart = Images.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(depart)


    if requset.method == 'GET':
        serializer = Imagesserializer(depart)
        return Response(serializer.data)


    if requset.method == 'PUT':
        serializer = Imagesserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_201_CREATED)


    if requset.method == 'DELETE':
        depart.delete()
        departS = Images.objects.all()
        serializer = Imagesserializer(departS,many=True)
        return Response(serializer.data)


'''
class Departserializers(APIView):
    def get(self, request, format=None):
        depart = Depart.objects.all()
        serializerd = Departserializer(depart, many=True)
        return Response(serializerd.data)

    def post(self, request, format=None):
        serializer = Departserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
'''

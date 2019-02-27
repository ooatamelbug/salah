from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from salah.serializer import Departserializer ,Productsserializer , Imagesserializer, Userserializer
from rest_framework.decorators import api_view , permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework.permissions import IsAdminUser
from salah.models import Depart , Products, Images
from django.contrib.auth import authenticate , login

# Create your views here.

@api_view(['GET'])
def DepartserializersG(request):
    if request.method == 'GET':
        departall = Depart.objects.all()
        serializer = Departserializer(departall,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def DepartserializersGd(request,pk):
    try:
        departalld = Depart.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Departserializer(departalld)
        return Response(serializer.data)



@csrf_exempt
@api_view(['POST'])
def Departserializers(request):
    if request.method == 'POST':
        serializer = Departserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)




@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def Departserializersd(request, pk):
    try:
        depart = Depart.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        depart.delete()
        departS = Depart.objects.all()
        serializer = Departserializer(departS,many=True)
        return Response(serializer.data)

    elif request.method == 'GET':
        serializer = Departserializer(depart)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = Departserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)



@api_view(['GET','POST'])
def Productsserializers(request):
    if request.method == 'POST':
        serializer = Productsserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        depart = Products.objects.all()
        serializer = Productsserializer(depart,many=True)
        return Response(serializer.data)



@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def Productsserializerd(request, pk):
    try:
        depart = Products.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(depart)


    if request.method == 'GET':
        serializer = Productsserializer(depart)
        return Response(serializer.data)


    if request.method == 'PUT':
        serializer = Productsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        depart.delete()
        departS = Products.objects.all()
        serializer = Productsserializer(departS,many=True)
        return Response(serializer.data)



@api_view(['GET','POST'])
def ImagesserializerS(request):
    if request.method == 'POST':
        serializer = Imagesserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        depart = Images.objects.all()
        serializer = Imagesserializer(depart,many=True)
        return Response(serializer.data)



@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def ImagesserializerD(request, pk):
    try:
        depart = Images.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(depart)


    if request.method == 'GET':
        serializer = Imagesserializer(depart)
        return Response(serializer.data)


    if request.method == 'PUT':
        serializer = Imagesserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        depart.delete()
        departS = Images.objects.all()
        serializer = Imagesserializer(departS,many=True)
        return Response(serializer.data)


'''
@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAdminUser,))
def login(request):
    username = request.data.get['username']
    password = request.data.get['password']
    if username is None or password is None:
        return Response({"errror":"error"},status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username,password=password)

    if not user:
        return Response({"errror":"invalid login"},status=HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key},status=HTTP_200_OK)



    '''
@api_view(['POST'])
def login(request):
    username = request.data.get['username']
    password = request.data.get['password']
    try:
        user = User.objects.get(name=username,password=password)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if user:
        userid = user['id']
        user = authenticate(name=username,password=password,id=userid)
        login(request,user)
        serializer = Userserializer(depart)
        return Response(serializer.data)






@api_view(['GET','PUT'])
def Userserializers(request,pk):
    try:
        user = User.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #serializer = Userserializer(user)
        #return Response(serializer.data)
        return JsonResponse(model_to_dict(user))

    if request.method == 'PUT':
        serializer = Userserializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)


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

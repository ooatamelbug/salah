from django.shortcuts import render
from django.http import JsonResponse
from django.http import response
#from django.http import request
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
#from rest_framework.views import APIView
from rest_framework.response import Response
from salah.serializer import Departserializer ,Productsserializer, Productsse , Imagesserializer
from rest_framework.decorators import api_view , permission_classes
#from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from salah.models import Depart , Products, Images
from django.contrib.auth import authenticate , login , logout

# Create your views here.


# Create function for get all depart .
@api_view(['GET'])
def DepartserializersG(request):
    if request.method == 'GET':
        departall = Depart.objects.all()
        serializer = Departserializer(departall,many=True)
        return Response(serializer.data)



# Create function for get one of depart .
@api_view(['GET'])
def DepartserializersGd(request,pk):
    try:
        departalld = Depart.objects.get(id=pk)
    except Depart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Departserializer(departalld)
        return Response(serializer.data)



# Create function for get all products .
@api_view(['GET'])
def Productsserializerg(request):
    if request.method == 'GET':
        product = Products.objects.all()
        serializer = Productsserializer(product,many=True)
        return Response(serializer.data)


#Create function for get one of product .
@api_view(['GET'])
def Productsserializert(request,pk):
    try:
        product = Products.objects.filter(depart=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Productsserializer(product,many=True)
        return Response(serializer.data)


# Create function for get one of product .
@api_view(['GET'])
def Productsserializergd(request,pk):
    try:
        product = Products.objects.get(id=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Productsserializer(product)
        return Response(serializer.data)



# Create function for create depart .
@api_view(['POST'])
def Departserializers(request):
    if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
        if request.method == 'POST':
            serializer = Departserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                depart = Depart.objects.all()
                serializer = Departserializer(depart,many=True)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'بيانات غير صحيحة'})
    return Response({'error':'not allowed'})




# Create function for     delete depart .
@api_view(['POST'])
def Departserializersd(request):
    if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
        if request.method == 'POST':
            depart = Depart.objects.get(id=request.data['idp'])
            depart.delete()
            departS = Depart.objects.all()
            serializer = Departserializer(departS,many=True)
            return Response(serializer.data)
        return Response({'error':'not allowed!!'})
    return Response({'error':'not allowed'})


# # Create function for get and update and delete depart .
# @api_view(['PUT'])
# def Departserializersp(request, pk):
#     if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
#
#         if request.method == 'PUT':
#             serializer = Departserializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
#         return Response({'error':'not allowed!!'})
#     return Response({'error':'not allowed'})
#


# Create function for create product .
@api_view(['POST'])
def Productsserializers(request):
    if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
        if request.method == 'POST':
            serializer = Productsse(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'بيانات غير صحيحة'})
        return Response({'error':'not allowed!'})
    return Response({'error':'not allowed!!!'})



# Create function for get and update and delete product .
@api_view(['POST'])
def Productsserializerd(request):
    if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
        if request.method == 'POST':
            id = request.data['idp']
            depart = Products.objects.get(id=id)
            depart.delete()
            departS = Products.objects.all()
            serializer = Productsserializer(departS,many=True)
            return Response(serializer.data)
    return Response({'error':'not allowed'})



# # Create function for get and update and delete product .
# @api_view(['GET','POST'])
# def Productsserializerup(request, pk):
#     if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
#         try:
#             depart = Products.objects.get(id=pk)
#         except Depart.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#         if request.method == 'GET':
#             serializer = Productsserializer(depart)
#             return Response(serializer.data)
#
#
#         if request.method == 'PUT':
#             serializer = Productsserializerd(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#     return Response({'error':'not allowed'})
#

# Create function for create images .
@api_view(['GET','POST'])
def ImagesserializerS(request):
    if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
        if request.method == 'POST':
            serializer = Imagesserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'بيانات غير صحيحة'})

        if request.method == 'GET':
            depart = Images.objects.all()
            serializer = Imagesserializer(depart,many=True)
            return Response(serializer.data)
    return Response({'error':'not allowed'})


#
# # Create function for get and update and delete images .
# @api_view(['GET','PUT','DELETE'])
# def ImagesserializerD(request, pk):
#     if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
#         try:
#             depart = Images.objects.get(id=pk)
#         except Depart.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         print(depart)
#
#
#         if request.method == 'GET':
#             serializer = Imagesserializer(depart)
#             return Response(serializer.data)
#
#
#         if request.method == 'PUT':
#             serializer = Imagesserializer(data=requset.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#
#         if request.method == 'DELETE':
#             depart.delete()
#             departS = Images.objects.all()
#             serializer = Imagesserializer(departS,many=True)
#             return Response(serializer.data)
#     return Response({'error':'not allowed'})



# Create function for login user .
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        count = User.objects.filter(username=username).count()
        if count == 0 :
            return Response({"error":" انت لست مستخدم"})
        else:
            usernamevalide = User.objects.get(username=username)
            passworduser = usernamevalide.password
            if usernamevalide:
                if check_password(password,passworduser):
                    user = authenticate(request,username=username,password=password)
                    if user is not None:
                        token, _ = Token.objects.get_or_create(user=user)
                        request.session['token'] = token.key
                        print(request.session['token'])
                        return Response({'token':request.session['token']})

                    return Response({"error":"انت لست مستخدم"})
                return Response({"error":"كلمة مرور غير صحيحة"})
            return Response({"error":" انت لست مستخدم"})

        # if not usernamevalide:
        #     return Response({"error":" انت لست مستخدم"})
    return Response({'error':'not allowed'})




# # Create function for get user details.
# @api_view(['GET','PUT'])
# def Userserializers(request,pk):
#     if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
#         try:
#             user = User.objects.get(id=pk)
#         except Depart.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'GET':
#             return JsonResponse(model_to_dict(user))
#
#         if request.method == 'PUT':
#             serializer = Userserializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
#     return Response({'error':'not allowed'})
#


# Create function for logout user .
@api_view(['POST'])
def logout(request):
    if request.data['token'] == '8dcb8ea967601761113feb25d24b477e331fff4e':
        if request.method == 'POST':
            request.session.flush()
            request.session.modified = True
            return Response({'sucess':'logout'})
        return Response({'error':'not allowed'})
    return Response({'error':'not allowed!!!'})



# 
# @api_view(['POST'])
# def UmagesserializerD(request):
#     if request.method == 'POST':
#         serializer = Umagesserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
#     return Response({'error':'not allowed'})

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

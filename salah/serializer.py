from rest_framework import serializers
from salah.models import Depart , Products, Images, User


class Departserializer(serializers.ModelSerializer):
    class Meta:
        model = Depart
        fields = ('id','name')

class Imagesserializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id','link')


class Productsserializer(serializers.ModelSerializer):
    depart = Departserializer()
    images__link = Imagesserializer(source='images_set',many=True)
    class Meta:
        model = Products
        #fields = '__all__'
        fields = ('name','price','currency','quantity','discount','date','discounttime','describ','depart','images__link')


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','password')

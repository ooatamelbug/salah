from rest_framework import serializers
from salah.models import Depart , Products, Images


class Departserializer(serializers.ModelSerializer):
    class Meta:
        model = Depart
        fields = ('id','name')

class Imagesserializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        #fields = ('id','link')


class Productsse(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =  '__all__'


class Productsserializer(serializers.ModelSerializer):
    depart = Departserializer()
    images__link = Imagesserializer(source='images_set',many=True)
    class Meta:
        model = Products
        #fields = '__all__'
        fields = ('id','name','price','currency','quantity','discount','date','discounttime','describ','depart','images__link')

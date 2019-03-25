from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from salah import views

'''
urlpatterns = [
    path('depart/',views.Departserializers.as_view()),
]
'''
urlpatterns = [
    path('depart/',views.Departserializers),
    path('departall/',views.DepartserializersG),
    #path('depart/<int:pk>/',views.Departserializersp),
    path('depart/delete/',views.Departserializersd),
    path('departall/<int:pk>/',views.DepartserializersGd),
    path('product/',views.Productsserializers),
    path('productall/',views.Productsserializerg),
    path('productallt/<int:pk>/',views.Productsserializert),
    path('productall/<int:pk>/',views.Productsserializergd),
    path('product/delete/',views.Productsserializerd),
    #path('product/<int:pk>/',views.Productsserializerup),
    path('image/',views.ImagesserializerS),
    #path('image/<int:pk>/',views.ImagesserializerD),
    path('adminprofile/',views.login),
    #path('adminprofile/<int:pk>/',views.Userserializers),
    path('logout/',views.logout),
]


urlpatterns = format_suffix_patterns(urlpatterns)

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
    path('depart/<int:pk>/',views.Departserializersd),
    path('departall/<int:pk>/',views.DepartserializersGd),
    path('product/',views.Productsserializers),
    path('product/<int:pk>/',views.Productsserializerd),
    path('image/',views.ImagesserializerS),
    path('image/<int:pk>/',views.ImagesserializerD),
    path('adminprofile/',views.login),
    path('adminprofile/<int:pk>/',views.Userserializers),
]
#urlpatterns = format_suffix_patterns(urlpatterns)

from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .serializers import *
from .models import *
from .middlewares import *


class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentView(APIView):
#     authentication_classes = [Authenticate]
#     # permission_classes = [StudentPermissions]
#     def get(self, request):
#         studentSerializer = StudentSerializer(Student.objects.all(), many=True)
#         return Response(studentSerializer.data)

#     def post(self, request):
#         studentSerializer = StudentSerializer(data=request.data)
#         if studentSerializer.is_valid():
#             studentSerializer.save()
#             return Response(studentSerializer.data)
#         return Response(studentSerializer.errors)

class ParentView(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializers

# class ParentView(APIView):
#     # authentication_classes = [Authenticate]
#     # permission_classes = [StudentPermissions]
#     def get(self, request):
#         parent = ParentSerializers(Parent.objects.all(), many=True)
#         return Response(parent.data)

#     def post(self, request):
#         parent = ParentSerializers(data=request.data)
#         if parent.is_valid():
#             parent.save()
#             return Response(parent.data)
#         return Response(parent.errors)
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from anything.models import Students
from anything.serializer import StudentSerializer


# Create your views here.
@api_view(['POST'])
def save(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch(request):
    # Students.objects.create(name="Camaro John",
    #                         email="camaro@gmail.com",
    #                         password="986tk",
    #                         gender="male",
    #                         sports="hockey",
    #                         education="college",)
    students = Students.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
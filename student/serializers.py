from wsgiref import validate
from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError

def checkMarks(value):
    if value < 0:
        raise ValidationError("marks must be greater than or equal to 0")

def checkName (value):
    if not value.isalpha():
        raise ValidationError("name must be only alpha")
        


class StudentSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(max_length = 100 , validators = [checkName])
    lastName  = serializers.CharField(max_length = 100, validators = [checkName]) 
    marks     = serializers.IntegerField(validators = [checkMarks])
    age       = serializers.IntegerField()
    
    
    class Meta():
        model = Student
        fields ='__all__'

class ParentSerializers(serializers.ModelSerializer):
    firstName = serializers.CharField(max_length = 100 , validators = [checkName])
    lastName  = serializers.CharField(max_length = 100, validators = [checkName])
    students = StudentSerializer(many = True)
    
    class Meta():
        model = Parent
        fields ='__all__'
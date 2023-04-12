from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from testapp.models import six,seven,eight,nine,ten,CurrentAffairs,GeneralKnowledge

class SixSerializers(serializers.ModelSerializer):
    class Meta:
        model=six
        fields='__all__'

class SevenSerializers(serializers.ModelSerializer):
    class Meta:
        model=seven
        fields='__all__'

class EightSerializers(serializers.ModelSerializer):
    class Meta:
        model=eight
        fields='__all__'

class NineSerializers(serializers.ModelSerializer):
    class Meta:
        model=nine
        fields='__all__'

class TenSerializers(serializers.ModelSerializer):
    class Meta:
        model=ten
        fields='__all__'        

class CurrentSerializers(serializers.ModelSerializer):
    class Meta:
        model=CurrentAffairs
        fields='__all__'     

class GeneralSerilizers(serializers.ModelSerializer):
    class Meta:
        model=GeneralKnowledge
        fields='__all__'           


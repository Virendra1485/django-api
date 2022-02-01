from rest_framework import serializers
from .models import StudentTbl


class StudentTblGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTbl
        fields = ['id', 'first_name', 'last_name', 'mobile', 'city', 'userid', 'password']


class StudentTblPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTbl
        fields = ['first_name', 'last_name', 'mobile', 'city', 'userid', 'password']


class StudentTblPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTbl
        fields = ['first_name', 'last_name', 'mobile', 'city', 'password']


class loginPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTbl
        fields = ['userid', 'password']
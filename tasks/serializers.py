from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=[
            'id',
            'title',
            'description',
            'priority',
            'completed',
            'created_at',
            'updated_at',   
            'due_date',
            'category',     
        ]
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'])
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
        return data
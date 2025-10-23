from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

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
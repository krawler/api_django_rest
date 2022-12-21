from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Category
        fields = '__all__'
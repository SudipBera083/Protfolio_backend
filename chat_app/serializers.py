from rest_framework import serializers
from .models import ChatResponse

class ChatResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatResponse
        fields = '__all__'

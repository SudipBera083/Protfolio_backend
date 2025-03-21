from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import UserResponse
from .serializers import UserResponseSerializer

@api_view(['POST'])
def submit_response(request):
    if request.method == 'POST':
        serializer = UserResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Response submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

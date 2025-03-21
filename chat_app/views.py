from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChatResponse
from .serializers import ChatResponseSerializer
import bonggoQuery


def bonggoChat(msg):
    return bonggoQuery.Query.normal_query.printing(msg)
    


@api_view(['POST'])
def chatbot(request):
    user_message = request.data.get("message", "").lower()
    return Response({"reply": bonggoChat(user_message)})

    # # Check if message exists in database
    # try:
    #     response = ChatResponse.objects.get(question=user_message)
    #     return Response({"reply": response.answer})
    # except ChatResponse.DoesNotExist:
    #     return Response({"reply": "Sorry, I don't understand. Can you rephrase?"})

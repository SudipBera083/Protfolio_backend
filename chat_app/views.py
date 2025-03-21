from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChatResponse
from .serializers import ChatResponseSerializer
import wolframalpha as wf
import wikipedia


app = wf.Client("3YEQYW-RA6A8LREGV")

          
def wikiLogic(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    return results



def bonggoChat(msg):
    querys= msg.lower()
    res = app.query(msg)
    try: 
        return f"{(next(res.results).text)}"
    except Exception:
        try:
            return f"According to Wikipedia {wikiLogic(querys)}"
        except Exception:
             return "There is an error !"
    


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

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_client.agent import run_agent
from api_client.models import ChatSession
from .models import ChatLog
from django.shortcuts import render 

class ChatAPIView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        session_id = request.data.get("session_id")
        
        if not user_message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create a session
        if session_id:
            session = ChatSession.objects.filter(id=session_id).first()
        else:
            session = ChatSession.objects.create(user_identifier="Demo User")

        if not session:
            return Response({"error": "Invalid session"}, status=status.HTTP_404_NOT_FOUND)

        # Log user message
        ChatLog.objects.create(session=session, role="user", content=user_message)

        # Run the Agent
        try:
            ai_response = run_agent(user_message)
            # Log AI message
            ChatLog.objects.create(session=session, role="assistant", content=ai_response)
            return Response({
                "session_id": session.id,
                "response": ai_response
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ChatUIView(APIView):
    def get(self, request):
        return render(request, 'index.html')
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ManApi.models import User
from .serializers import TaskSerializer


# Create your views here.

class UserListView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = TaskSerializer(user, many=True)
        data = {
            'ok': True,
            'members': serializer.data
        }
        return JsonResponse(data)

class UserListViewApi(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = TaskSerializer(user, many=True)
        data = {
            'ok': True,
            'members': serializer.data,
        }
        return Response(data)

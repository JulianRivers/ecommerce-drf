from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,  HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class UserAPIView(APIView):

    def get(self, request):
        query = User.objects.all()
        users_serializer = UserSerializer(query, many = True)
        return Response(users_serializer.data)

@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        query = User.objects.all()
        users_serializer = UserSerializer(query, many = True)
        return Response(users_serializer.data, status=HTTP_200_OK)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, HTTP_201_CREATED)
        return Response(user_serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def user_detail_api_view(request, pk=None):
    #Queryset
    user = User.objects.filter(id = pk).first()

    if user:
        # Retrive
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=HTTP_200_OK)
            return Response(user_serializer.errors, status=HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Eliminado correctamente'}, status=HTTP_204_NO_CONTENT)

    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=HTTP_404_NOT_FOUND)

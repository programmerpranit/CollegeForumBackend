import datetime, jwt
import email
from rest_framework.views import APIView

from CollegeForum.settings import SECRET_KEY
from .util.gauth import getSub
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


def verifyUser(token):
    try:
        decodedToken = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = User.objects.filter(sub = decodedToken['sub']).first()
        return user
    except jwt.ExpiredSignatureError:
        return None


@api_view(['POST'])
def authenticate(request): 

    gTokenId = request.data['gtoken']
    data = getSub(gTokenId)
    if data is None:
        return Response({'error': 'Invalid Id Token'}, status=status.HTTP_400_BAD_REQUEST)

    payload = {
        'sub': data['sub'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    user = User.objects.filter(sub = data['sub']).first()

    if user is None:
        user = User.objects.create(sub = data['sub'], username = data['sub'], email= data['email'])
        user.save()
        return Response({'token': token}, status=status.HTTP_201_CREATED)
    else:
        return Response({'token': token}, status=status.HTTP_200_OK)


class UserView(APIView):

    def get(self, request):
        user = verifyUser(request.data['jwttoken'])
        if user is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

        userSerializer = UserSerializer(user)
        return Response(userSerializer.data, status=status.HTTP_200_OK)

    # for editing user info
    # require auth 
    def post(self, request):
        user = verifyUser(request.data['jwttoken'])
        if user is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user.prn = request.data.get('prn')
            user.name = request.data.get('name')
            user.year_of_study = request.data.get('year_of_study')
            user.save()
        except:
            return Response({'error': 'Unknown error occured Please check your PRN Number. It needs to be unique'}, status=status.HTTP_400_BAD_REQUEST)

        newUser = UserSerializer(user, partial=True)
        

        return Response(newUser.data, status=status.HTTP_201_CREATED)

    




import datetime, jwt
from rest_framework.views import APIView
from .util.gauth import getSub
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def authenticate(request): 

    gTokenId = request.data['gtoken']
    sub = getSub(gTokenId)
    if sub is None:
        return Response({'error': 'Invalid Id Token'}, status=status.HTTP_400_BAD_REQUEST)

    payload = {
        'sub': sub,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, 'myseceratekey', algorithm='HS256')

    user = User.objects.filter(sub = sub).first()
    if user is None:
        user = User.objects.create(sub = sub, username = sub)
        user.save()
        return Response({'token': token}, status=status.HTTP_201_CREATED)
    
    else:
        return Response({'token': token}, status=status.HTTP_200_OK)


class UserView(APIView):

    def get(self, request):
        token = request.data['jwttoken']
        decodedToken = jwt.decode(token, 'myseceratekey', algorithms=['HS256'])

        user = User.objects.filter(sub = decodedToken['sub']).first()

        if user is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            userSerializer = UserSerializer(user)
            return Response(userSerializer.data, status=status.HTTP_200_OK)



    # for editing user info
    # require auth
    def put(self, request):
        # token = request.data['jwttoken']
        # decode token
        # get sub from it
        # if valid:
        #     user = User.objects.get(sub = sub)
        #     user.name = request.data['name']
        #     user.save()
        pass

    




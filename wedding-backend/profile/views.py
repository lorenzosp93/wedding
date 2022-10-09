from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def setup_plus_one(request):
    "View to set up a plus one for a user"
    user = request.user
    if request.data:
        data = request.data
        user, created = user.profile.setup_plus_one(
            data['first_name'],
            data['last_name'],
            data['email']
        )
        if (user is not None) & created: 
            return Response(
                status=200,
                data=f"User {user.email} created",
            )
        elif user:
            return Response(
                status=500,
                data=f"User {user.email} exists already",
            )
        return Response(
            status=400,
            data="No plus-one available",
        )
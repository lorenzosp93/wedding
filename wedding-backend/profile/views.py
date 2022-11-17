from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PlusOneSerializer

# Create your views here.


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def setup_plus_one(request):
    "View to set up a plus one for a user"
    serializer = PlusOneSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        data = serializer.validated_data
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
                data={"non_field_errors": f"User {user.email} exists already"},
            )
        return Response(
            status=400,
            data={"non_field_errors": "No plus-one available"},
        )
    return Response(
        status=500,
        data=serializer.errors
    )

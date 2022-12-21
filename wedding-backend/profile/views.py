from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import PlusOneSerializer, RegisterUserSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny,))
def register_user(request: Request) -> Response:
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.user
        data = serializer.validated_data
        if user and isinstance(user, AbstractUser) and user.email == '':
            try:
                user.email = user.username = data.get('email')
                user.save()
            except:
                return Response(
                    status=500,
                    data={"non_field_errors": _("An error occurred creating your profile, please try again later.")},
                )
            return Response(
                status=201,
                data=_("Profile created successfully, please proceed with login."),
            )
        return Response(
            status=200,
            data=_("Profile already exists, please proceed with login."),
        )
    return Response(
        status=400,
        data=serializer.errors,
    )


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def setup_plus_one(request: Request) -> Response:
    "View to set up a plus one for a user"
    serializer = PlusOneSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        data = serializer.validated_data
        user, created = user.profile.setup_plus_one(
            data['first_name'],
            data['last_name'],
            data['email'],
        )
        if (user is not None) & created:
            return Response(
                status=201,
                data=_("User %(email)s created" % {'email': user.email}),
            )
        elif user:
            return Response(
                status=400,
                data={"non_field_errors": _("User %(email)s exists already" % {'email': user.email})},
            )
        return Response(
            status=400,
            data={"non_field_errors": _("No plus-one available")},
        )
    return Response(
        status=400,
        data=serializer.errors
    )

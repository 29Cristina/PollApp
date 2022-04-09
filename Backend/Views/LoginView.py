from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Backend.Serializers.LoginSerializer import LoginSerializer
from rest_framework import generics, serializers, views, status

class LoginView(views.APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        request=LoginSerializer,
    )
    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
        if serializer.is_valid():
            serializer.save(serializer.validated_data)
            return Response(None, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
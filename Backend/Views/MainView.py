from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def MainView(response):
    s="/choices and choice/nr \n votes and vote/nr \n"
    return Response(s)





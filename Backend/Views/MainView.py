

from django.http import HttpResponse


def detail(response):
    s="/choices and choice/nr \n votes and vote/nr \n"
    return HttpResponse(s)





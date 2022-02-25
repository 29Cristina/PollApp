from django.http import HttpResponse


def MainView(response):
    s="/choices and choice/nr \n votes and vote/nr \n"
    return HttpResponse(s)





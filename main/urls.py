"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Backend.Views.MainView import MainView
from Backend.Views.ChoiceView import ChoiceList, ChoiceDetail
from Backend.Views.ExampleView import ExampleList, ExampleDetail
from Backend.Views.PollView import PollDetail, PollList
from Backend.Views.VoteView import VoteList, VoteDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('choices/', ChoiceList.as_view()),
    path('choices/<int:pk>', ChoiceDetail.as_view()),
    path('votes/', VoteList.as_view()),
    path('vote/<int:pk>', VoteDetail.as_view()),
    path('examples/', ExampleList.as_view()),
    path('example/<int:pk>', ExampleDetail.as_view()),
    path('polls/', PollList.as_view()),
    path('poll/<int:pk>', PollDetail.as_view()),
    path('', MainView),
]
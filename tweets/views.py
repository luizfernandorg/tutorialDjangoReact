from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view(request, tweet_id):
    print("Tweet id %d" % (tweet_id,))
    return HttpResponse("Hello World!")
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view(request, tweet_id):
    return HttpResponse(f"Hello World! {tweet_id}")
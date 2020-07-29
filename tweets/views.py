from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from tweets.models import Tweet

def home_view(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"tweets/home.html",context={},status=200)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavasScript/Swift/Java/iOS/Android
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    print(tweets_list)
    data = {
        'response' : tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id):
    """
    REST API VIEW
    Consume by JavasScript/Swift/Java/iOS/Android
    return json data
    """
    data = {}
    status = 200
    try: 
        obj = Tweet.objects.get(id=tweet_id)
        data['id'] = obj.id
        data['content'] = obj.content
        # data['image'] = obj.image.url
    except:
        data['message'] = "Not found"
        status = 404

    #return HttpResponse(f"Hello World! {tweet_id} - {obj.content}")
    return JsonResponse(data, status=status) # could use HttpResonse, with json.dumps and content_type='application/json'
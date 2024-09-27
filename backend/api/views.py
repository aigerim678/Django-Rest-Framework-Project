import json
from django.http import JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    # print(request.GET) # url query params
    # print(request.POST)
    # body = request.body # byte string of JSON data
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    
    # try:
    #     data = json.loads(body) # string of JSON data -> Python Dict
    # except:
    #     pass
    # print(data)
    # data['headers'] = request.headers # request.META ->
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type

    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
    #return JsonResponse({"message": "Hi there, this is your Django API response!!"})

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


def post_list(request, user_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET',])
    return JsonResponse({"status" : "OK"})

@csrf_exempt
def create(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST',])
    return JsonResponse({"new_id" : request.POST['new_id']})

# Create your views here.

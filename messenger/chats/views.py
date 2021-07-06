from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Chat, Message
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import MessageSerializer, ChatSerializer
from rest_framework.response import Response
from blogs.models import User
from functools import wraps
from django.core.cache import cache


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0].request.user.is_authenticated:
            return func(*args, **kwargs)
        else:
            print(args[0].request.path)
            cache.set('login-url', args[0].request.path)
            print(cache.get('login-url'))
            return HttpResponseRedirect(
                    redirect_to='/login/')
    return wrapper


class ChatsViewSet(viewsets.ViewSet):
    """
    API endpoint that allows chats to be viewed or edited.
    """
    queryset = Chat.objects.all()
    user = User

    @login_required
    def list(self, request):
        if cache.get(str(request.user.id), 0) == 0:
            c = cache.get('users_in_system', 0)
            cache.set('users_in_system', c + 1)
            cache.set(str(request.user.id), 1)
        else:
            c = cache.get('users_in_system', 0)
            cache.set('users_in_system', c)
        queryset = Chat.objects.filter(users=request.user)
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    @login_required
    def retrieve(self, request, pk=None):
        queryset_chat = Chat.objects.filter(users=request.user)
        chat = get_object_or_404(queryset_chat, pk=pk)
        serializer_chat = ChatSerializer(chat)
        queryset_message = Message.objects.filter(
                chat__id=pk)
        serializer_message = MessageSerializer(queryset_message, many=True)
        return Response([
            serializer_chat.data['title'],
            serializer_message.data
        ])

    @login_required
    def create(self, request):
        title = request.data
        chat = Chat.objects.create(title=title)
        chat.users.add(request.user)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    @login_required
    def update(self, request, pk=None):
        content = request.data
        message = Message.objects.create(
            chat=Chat.objects.get(id=pk),
            content=content,
            user=request.user
        )
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    @login_required
    def delete(self, request, pk=None):
        Chat.objects.filter(id=pk).delete()
        return Response()


"""
def page(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return render(request, 'chats/hello.html')
"""


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')

# Create your views here.

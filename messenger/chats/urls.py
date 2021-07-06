from chats.views import ChatsView, chat_detail, page, create, delete, update
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', ChatsView.as_view({'get': 'list'}), name='chat_list'),
    path('page/', page, name='page'),
    path('create/', create, name='create'),
    path('delete/', delete, name='delete'),
    path('update/', update, name='update'),
    path('<int:chat_id>/', chat_detail, name='chat_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)

from blogs.views import create, post_list
from django.urls import path

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:user_id>/', post_list, name='post_list')
]

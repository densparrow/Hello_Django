from django.shortcuts import render
from .models import Post


# Create your views here.
# 1. blog_index отобразит список всех ваших сообщений( будет содержать orderby() по полю created_on в обратном порядке )
# 2. blog_detail отобразит полный конкретное сообщение
# Подсказка
# Эти функции будет почти эквивалентны функциям просмотра в projects приложении

def blog_index(request):
    posts = Post.objects.order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def project_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog_detail.html', context)
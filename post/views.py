from django.shortcuts import render

# Create your views here.ъ
# здесь настроивается отображение данных
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', context={'post': posts})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import  Post
# Create your views here.

#글 목록보기
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''<h1>Hello {myname}</h1>
    # '''.format(myname=name))

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return  render(request, 'blog/post_list.html',{'posts':posts})
# 글 상세조회


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})


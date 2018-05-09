from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from blog.modelforms import PostModelForm, PostForm
from blog.models import Post

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

#글 등록

def post_new(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm()
        print(form)


    return render(request, 'blog/post_edit.html',{'form':form})

#글등록 폼을 사용
def post_new_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            post = Post()
            post.author = request.user
            post.title = form.cleaned_data["title"]
            post.text = form.cleaned_data["text"]
            post.published_date = timezone.now()
            post.save()
            # post = Post.objects.create(author = request.user, title = form.cleaned_data["title"], text = form.cleaned_data["text"],published_date = timezone.now())

            return redirect('post_detail', pk=post.pk)
        else:
            print(form.errors)
    else:
        form = PostForm()
    return  render(request, 'blog/post_form.html',{'form':form})

#글 수정//modelform 사용
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostModelForm(instance=post)

    return render(request, 'blog/post_edit.html',{'form':form})

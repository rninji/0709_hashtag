from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from .forms import PostForm, TagForm

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts_list':posts})

def new(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')

    else:
        form=PostForm()
        tag_form=TagForm()
    return render(request,'new.html',{'form':form, 'tag_form':tag_form})

def detail(request, index):
    post=get_object_or_404(Post,pk=index)
    return render(request, 'detail.html',{'post':post})

def delete(request,pk):
    item=get_object_or_404(Post,pk=pk)
    item.delete()
    return redirect('home')

def tag_add(request,pk):
    post=get_object_or_404(Post,pk=pk)
    tag_form=TagForm(request.POST)
    if tag_form.is_valid():
            tag=tag_form.save(commit=False)
            tag, created = Tag.objects.get_or_create(name=tag.name)
            post.tags.add(tag)
            return redirect('detail',index=pk)

def tag_home(request):
    tags=Tag.objects.all()
    return render(request,'tag.html',{'tags':tags})

def tag_detail(request,pk):
    tag=get_object_or_404(Tag,pk=pk)
    tag_posts=tag.post_set.all()
    return render(request,'tag_detail.html',{'tag':tag,'tag_posts':tag_posts})

def tag_delete(request, pk, tag_pk):
	post = get_object_or_404(Post, pk=pk)
	tag = get_object_or_404(Tag, pk=tag_pk)
	post.tags.remove(tag)
	if tag.post_set.count() == 0 :
		tag.delete()
	return redirect('detail', pk=pk)
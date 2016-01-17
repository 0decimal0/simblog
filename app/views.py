from django.shortcuts import render,render_to_response,get_object_or_404

# Create your views here.
from django.http import HttpResponse


def index(request):
        return render_to_response('index.html',{
            'categories':Category.objects.all(),
            'posts':Blog.objects.all()[:5]
            },context_instance=RequestContext(request))

def view_post(request,slug):
    return render_to_response('view_post.html',{
        'post':get_object_or_404(Blog,slug = slug)
        },context_instance=RequestContext(request))

def view_category(request,slug):
    category = get_object_or_404(Category,slug = slug)
    return render_to_response('view_category.html',{
        'category':category,
        'posts':Blog.objects.filter(category=category)[:5]
        })

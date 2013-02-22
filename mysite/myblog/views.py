# Create your views here.
from django.http import HttpResponse
from myblog.models import BlogPost
from django.shortcuts import render_to_response

def index(request):
    posts = BlogPost.objects.all()
    return render_to_response('myblog/index.html', {'posts': posts})
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def getALlPosts(request):
    try:    
        posts = Post.objects.all()
        serializedPosts = PostSerializer(posts, many=True)
        return Response(serializedPosts.data)
    except:
        return HttpResponse("No posts found")

@api_view(["GET"])
def getPost(request,id):
    try:
        post = Post.objects.get(id=id)
        serializedPost = PostSerializer(post)
        return Response(serializedPost.data)    
    except:
        return Response("No post found")

@api_view(["POST"])
def createPost(request):
    serializedPost = PostSerializer(data = request.data)
    if serializedPost.is_valid():
        serializedPost.save()
        return Response(serializedPost.data)
    else:
        return Response(serializedPost.errors, status=400)

@api_view(["PUT", "PATCH"])
def updatePost(request, id):
    try:
        post = Post.objects.get(id=id)
        serializedPost = PostSerializer(instance=post, data=request.data, partial=(request.method == "PATCH"))
        if serializedPost.is_valid():
            serializedPost.save()
            return Response(serializedPost.data)
    except:
        return Response("Invalid data")

@api_view(["DELETE"])
def deletePost(request, id):
    try:
        post = Post.objects.get(id = id)
        post.delete()
        return Response("Post deleted")
    except:
        return Response("No post found")

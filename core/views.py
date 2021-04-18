from django.shortcuts import render
from django.http import JsonResponse , HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


class TestView(APIView):
    def get(self , *args, **kwargs):

        qs = Post.objects.all()
        serializer = PostSerializer(qs, many = True)

        return Response(serializer.data)

    def post(self , *args, **kwargs):
        serializer = PostSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


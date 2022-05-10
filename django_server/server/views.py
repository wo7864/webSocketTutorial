from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.



class View(APIView):

    # 조회
    def get(self, request):
        return Response(status=200)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny


class GetServerDetails(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = ServerInventory.objects.all()
        ser = ServerDetailsSerializer(qs, many=True)
        return Response(ser.data)
        

class GetServer(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        qs = ServerInventory.objects.all()
        ser = ServerDetailsSerializer(qs, many=True)
        return Response(ser.data)
        
from django.shortcuts import render
from django.http import HttpResponse
from .models import Files
from rest_framework import viewsets
from .serializers import FilesSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer



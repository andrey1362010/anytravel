# Create your views here.
from django.http      import HttpResponse
from django.shortcuts import render, redirect

def index( request ):
    return render( request, 'index.html' )

def registration( request ):
    return render( request, 'registration/index.html' )
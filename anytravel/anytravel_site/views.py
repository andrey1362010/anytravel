# Create your views here.
from django.http      import HttpResponse
from django.shortcuts import render, redirect
from anytravel_site   import models

from django.contrib.auth.models import User
from django.contrib.auth        import authenticate, login, logout
from django.contrib             import messages

def index( request ):
    return render( request, 'index.html' )

def signin ( request ):
    if request.user.is_authenticated(): return redirect('/')

    if request.POST:
        try:
            email  = request.POST['email']
            passwd = request.POST['passwd']
        except:
            return redirect('/')

        user = authenticate( username = email, password = passwd )

        if user is not None:
            login( request, user )
        else:
            messages.error( request, 'NOT_SIGNIN' )

    return redirect('/')

def signout ( request ):
    if request.user.is_authenticated():
        logout( request )

    return redirect('/')

def registration( request ):
    if request.user.is_authenticated(): return redirect('/')

    if request.POST:
        email     = request.POST['email']
        passwd    = request.POST['passwd']
        passwdrpt = request.POST['passwdrpt']

        if email == "" or email is None:
            messages.error( request, 'EMPTY_EMAIL'     )
            return redirect('/registration/')

        if passwd == "" or passwd is None:
            messages.error( request, 'EMPTY_PASSWD'    )
            return redirect('/registration/')

        if passwdrpt == "" or passwdrpt is None:
            messages.error( request, 'EMPTY_PASSWDRPT' )
            return redirect('/registration/')

        if passwdrpt != passwd:
            messages.error( request, 'PASSWDS_NOT_MATCH' )
            return redirect('/registration/')

        try:
            u = User.objects.create_user( username = email, password = passwd )
            u.save()
        except:
            messages.error( request, 'CANT_CREATE_USER' )
            return redirect('/registration/')

        messages.success( request, 'SUCCESS_CREATE_USER' )
        return redirect('/registration/')

    return render( request, 'registration/index.html' )
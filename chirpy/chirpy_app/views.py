from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from chirpy_app.forms import AuthenticateForm, UserCreateForm, ChirpyForm
from chirpy_app.models import Chirpy


def index(request, auth_form=None, user_form=None):
    # index view, we first check if the user is logged
    if request.user.is_authenticated():
        chirpy_form = ChirpyForm()
        user = request.user
        chirpy_self = Chirpy.objects.filter(user=user.id)
        chirpy_buddies = Chirpy.objects.filter(user__userprofile__in=user.profile.follows.all)
        chirpy = chirpy_self | chirpy_buddies

        return render(request,
                      'buddies.html',
                      {'chirpy_form': chirpy_form, 'user': user,
                       'chirpy': chirpy,
                       'next_url': '/',  })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })


def login_view(request):    #code to log in/out the user. 
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):  #deletes the session and logs the user out
    logout(request)
    return redirect('/')


def signup(request):       #the user is saved to the database, authenticated, logged in and then redirected to the home page
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')


@login_required         
def public(request, chirpy_form=None):
    chirpy_form = chirpy_form or ChirpyForm()
    chirpy = Chirpy.objects.reverse()[:10]     #query the database for the last 10 posts
    return render(request,
                  'public.html',
                  {'chirpy_form': chirpy_form, 'next_url': '/chirpy',
                   'chirpy': chirpy, 'username': request.user.username})


@login_required				#decorator, which executes the function only if the user is authenticated else redirected
def submit(request):
    if request.method == "POST":
        chirpy_form = ChirpyForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if chirpy_form.is_valid():
            chirpy = chirpy_form.save(commit=False)
            chirpy.user = request.user
            chirpy.save()
            return redirect(next_url)
        else:
            return public(request, chirpy_form)
    return redirect('/')


def get_latest(user):
    try:
        return user.chirpy_set.order_by('id').reverse()[0]
    except IndexError:
        return ""


@login_required
def users(request, username="", chirpy_form=None):    #only logged in users are able to view profiles
    if username:
        # Show a profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        chirpy = Chirpy.objects.filter(user=user.id)
        superUser = User.objects.get(id=user.id)
        if username == request.user.username or request.user.profile.follows.filter(user__username=username):
            # Self Profile
           return render(request, 'user.html', {'user': user, 'chirpy': chirpy, 'follows' : superUser.profile.follows.all() , 'followers' : superUser.profile.followed_by.all() })
        return render(request, 'user.html', {'user': user, 'chirpy': chirpy, 'follow': True, })
    users = User.objects.all().annotate(chirpy_count=Count('chirpy'))
    chirpy = map(get_latest, users)
    obj = zip(users, chirpy)
    chirpy_form = chirpy_form or ChirpyForm()
    return render(request,
                  'profiles.html',
                  {'obj': obj, 'next_url': '/users/',
                   'chirpy_form': chirpy_form,
                   'username': request.user.username, })


@login_required
def follow(request):		#follow parameter passed by post method
    if request.method == "POST":
        follow_id = request.POST.get('follow', False)
        if follow_id:
            try:
                user = User.objects.get(id=follow_id)
                request.user.profile.follows.add(user.profile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')

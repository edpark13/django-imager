# from django.
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from imager_images.models import get_random_picture


def home(request):
    context = {}
    picture = get_random_picture()
    context = {'picture': picture}
    try:
        if request.user.profile:
            return profile(request)
    except AttributeError:
        return render(request, 'home.html', context)
        

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def profile(request):
    profile = request.user.profile
    num_picture = profile.num_of_photos()
    num_albums = profile.num_of_albums()
    num_followers = len(profile.followers())
    context = {'profile': profile, 'num_pictures': num_picture,
               'num_albums': num_albums, 'num_followers': num_followers}
    return render(request, 'profile.html', context)


@login_required
def library(request):
    profile = request.user.profile
    picture = profile.photos.all()
    album = profile.albums.all()
    context = {'profile': profile, 'pictures': picture,
               'albums': album}
    return render(request, 'library.html', context)

@login_required
def stream(request):
    profile = request.user.profile
    photos = profile.get_stream_photos
    # yours = profile.get_profile_stream()[:20]
    # theres = profile.get_followers_stream()[:20]
    # context = {'profile': profile, 'yours': yours, 'theres': theres}
    context = {'profile': profile, 'photos': photos}
    return render(request, 'stream.html', context)

# def user_login(request):
#     # Like before, obtain the context for the user's request.
#     context = RequestContext(request)

#     # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':
#         # Gather the username and password provided by the user.
#         # This information is obtained from the login form.
#         username = request.POST['username']
#         password = request.POST['password']

#         # Use Django's machinery to attempt to see if the username/password
#         # combination is valid - a User object is returned if it is.
#         user = authenticate(username=username, password=password)

#         # If we have a User object, the details are correct.
#         # If None (Python's way of representing the absence of a value), no user
#         # with matching credentials was found.
#         if user:
#             # Is the account active? It could have been disabled.
#             if user.is_active:
#                 # If the account is valid and active, we can log the user in.
#                 # We'll send the user back to the homepage.
#                 login(request, user)
#                 return HttpResponse('You are Logged in')
#             else:
#                 # An inactive account was used - no logging in!
#                 return HttpResponse("Your Rango account is disabled.")
#         else:
#             # Bad login details were provided. So we can't log the user in.
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render_to_response('registration/login.html', {}, context)


# @login_required
# def user_logout(request):
#     # Since we know the user is logged in, we can now just log them out.
#     logout(request)

#     return HttpResponseRedirect('')

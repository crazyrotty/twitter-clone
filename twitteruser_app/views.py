from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser_app.models import TwitterUser
from tweet_app.models import Tweet
from notification_app.models import Notification
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    data = TwitterUser.objects.all()
    return render(request, "index.html", {'data': data})


def tweeter(request, username):
    if request.user.is_authenticated:
        tweeter = TwitterUser.objects.filter(username=username).first()
        post_list = Tweet.objects.filter(tweeter=tweeter).order_by("-post_time")
        following = tweeter.follows.all()
        my_following = request.user.follows.all()
        pings = Notification.objects.filter(receiver=request.user)
        return render(request, "profile.html", {"tweeter": tweeter, "post_list": post_list, "following": following, "my_following": my_following, "pings": pings})
    else:
        return HttpResponseRedirect('public')
        

def tweeter_view(request, username):
    tweeter = TwitterUser.objects.filter(username=username).first()
    post_list = Tweet.objects.filter(tweeter=tweeter).order_by("-post_time")
    return render(request, "profile.html", {"tweeter": tweeter, "post_list": post_list})

@login_required
def follow(request, tweeter_id):
    request.user.follows.add(TwitterUser.objects.get(id=tweeter_id))
    return HttpResponseRedirect(reverse("home"))

@login_required
def unfollow(request, tweeter_id):
    request.user.follows.remove(TwitterUser.objects.get(id=tweeter_id))
    return HttpResponseRedirect(reverse("home"))

# Create your views here.

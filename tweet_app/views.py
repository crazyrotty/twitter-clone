from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from tweet_app.models import Tweet
from tweet_app.forms import TweetForm
from twitteruser_app.models import TwitterUser
from notification_app.models import Notification
import re

@login_required
def index(request):
    post_list = Tweet.objects.all().order_by('-post_time')
    pings = Notification.objects.filter(receiver=request.user)
    return render(request, "index.html", {"post_list": post_list, "pings": pings})


@login_required
def tweet_form(request):
    pings = Notification.objects.filter(receiver=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(body=data['body'], tweeter=request.user)
            if '@' in data['body']:
                recipient = re.findall(r'@(\w+)', data.get('body'))
                for receipt in recipient:
                    Notification.objects.create(msg_content=tweet, receiver=TwitterUser.objects.get(username=receipt))
            return HttpResponseRedirect(reverse('home'))
    form = TweetForm()
    return render(request, "generic.html", {"form": form, "pings": pings})


def tweet_detail(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Tweet, id=post_id)
        pings = Notification.objects.filter(receiver=request.user)
        return render(request, 'tweet.html', {'post': post, "pings": pings})


def public_tweet(request):
    all_users = TwitterUser.objects.all()
    post = []
    for author in all_users:
        all_post = Tweet.objects.filter(tweeter=author)
        for tweets in all_post:
            post.append(tweets.tweeter)
            post.append(tweets.body)
    return render(request, 'public_tweet.html', {'post': post})

# Create your views here.

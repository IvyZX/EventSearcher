from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.exceptions import ObjectDoesNotExist
from mainapp.models import *
from mainapp.fetch import *
from django.http import HttpResponse
from django.template import RequestContext
from ast import literal_eval

import threading
import time
import datetime
import json
from django.utils.safestring import mark_safe


def StartPage(request):
	context = RequestContext(request)
	return render_to_response('front.html', {}, context)

def MapPage(request):
    context = RequestContext(request)
    event_ids = []
    for t in Tweet.objects.all():
        if t.event_id not in event_ids:
            event_ids.append(t.event_id)
    names = []
    xs = []
    ys = []
    pops = []
    tweetlists = []
    for eid in event_ids:
        event = Event.objects.get(id=eid)
        names.append(str(event.name))
        xs.append(float(event.longitude))
        ys.append(float(event.latitude))
        tweets = []
        pop = 0
        for t in Tweet.objects.filter(event_id=eid):
            pic_url = unicode(str(t.pic_url)).encode('utf8')
            if (pic_url == 'None'):
                pic_url = ""
            tweets.append([unicode(t.author).encode('utf8'), unicode(t.text).encode("utf8"),
                           unicode(str(t.pub_date)).encode('utf8'), unicode(pic_url).encode('utf8')])
            pop = pop+t.num_retweet+1
        pops.append(pop)
        tweetlists.append(tweets)
    # produce popularity rank of tweets
    rank = [10, 50, 100]
    popranks = []
    leng = len(pops)
    for pop in pops:
        if (pop >= rank[-1]):
            popranks.append(4)
        elif (leng == 2) or (pop >= rank[-2]):
            popranks.append(3)
        elif (leng == 3) or (pop >= rank[-3]):
            popranks.append(2)
        else:
            popranks.append(1)

    return render_to_response('sample_map.html',
                              {'nameList': mark_safe(names),
                               'xList': xs, 'wyList': ys,
                               'tweetList': mark_safe(tweetlists), 'popList': popranks}, context)

def MainPage(request):
	context = RequestContext(request)
	xList = [41,41.1]
	yList = [-87.7, -87.8]
	nameList = mark_safe(["title1", "title2"])
	return render_to_response('sample_map.html', {'xList': xList, 'yList': yList, 'nameList': nameList}, context)

# this webpage will never be displayed until the for-loop is done; used to continuously fetch data
def GetData(request):
	for i in range(3):
		time.sleep(10)
		return HttpResponse("Start to fetch data.")


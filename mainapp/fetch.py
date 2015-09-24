from mainapp.models import *
from django.core.exceptions import ObjectDoesNotExist
import urllib2
import json
import tweepy
from tweepy import OAuthHandler
import datetime

def SearchFbEvents(query):
    fburl = 'https://graph.facebook.com/v2.2/'
    access_token='CAACEdEose0cBADozuJWZBm480ObqvssSDNc4CGYp5OgIkR9OhznSNvZB7Nddhe64NieGX0L3UKixzQZAeCLZBwlZAzZCru2vygfZBnHQUxodJVy2gIYehoS5B6sM0hV5djlpdScsN3EzvV3fE4hI8BTwmIRWgAkyZAQiP6fP6FoDoYQ92fAv4KiZAhhomBRTzgrFUFyYo9AliwFLTUB3QLrxG'
    fields='venue'
    url = fburl+'search?type=event&q='+query+'&access_token='+access_token+'&fields='+fields
    longitude=-87.6947
    latitude=42.0464
    content = urllib2.urlopen(url).read()       # a string of json objects
    events = json.loads(content)['data']
    id_list=[]
    longitude_list=[]
    latitude_list=[]
    return_list=[]

    for i in range(0,len(events)-1):
        longitude_list.append((events[i].get('venue', {})).get('longitude',0))
        latitude_list.append((events[i].get('venue', {})).get('latitude',0))
        if (abs(longitude_list[-1]-(longitude))<=1 and abs(latitude_list[-1]-(latitude))<=1 and (not events[i]['id'] in id_list)):
            id_list.append(events[i]['id'])
            id_url= fburl+'search?'+'id='+id_list[-1]+'&access_token='+access_token
            id_content=urllib2.urlopen(id_url).read()
            id_data = json.loads(id_content)['data']
            name= id_data[-1]['name']
            # return_list.append({'event':[id_list[-1],name,latitude_list[-1],longitude_list[-1]]})
            try:
                e = Event.objects.get(id=id_list[-1])
            except ObjectDoesNotExist:
                e = Event(id=id_list[-1], name=name, latitude=latitude_list[-1], longitude=longitude_list[-1],
                            start_date=datetime.datetime.utcnow(), end_date=datetime.datetime.utcnow())
                e.save()
        else:
            longitude_list.pop()
            latitude_list.pop()
    # return return_list


def FetchFbEvents():
    list_of_building_names=["Charles%20Deering%20Library","Seeley%20G.%20Mudd%20Science%20and%20Engineering%20Library","University%20Library","Dearborn%20Observatory","Technological%20Institute","University%20Hall","Alice%20Millar%20Chapel","Garrett%20Evangelical%20Theological%20Seminary","Levere%20Memorial%20Temple","Seabury%20Western%20Theological%20Seminary","Blomquist%20Recreation%20Center","Boat%20House","Byron%20S.%20Coon%20Sports%20Center","Henry%20Crown%20Sports%20Pavilion/Norris%20Aquatic%20Center","Lakeside%20Fields","Nicolet%20Football%20Center","Patten%20Gymnasium","Rocky%20Miller%20Park","Ryan%20Field","McGaw%20Memorial%20Hall/Shirley%20Welsh%20Ryan%20Arena","Trienens%20Hall","Mary%20and%20Leigh%20Block%20Museum%20of%20Art","Cahn%20Auditorium","Lutkin%20Memorial%20Hall","Marjorie%20Ward%20Marshall%20Dance%20Center","Pick%20Staiger%20Concert%20Hall","Regenstein%20Hall%20of%20Music","Theatre%20and%20Interpretation%20Center","Central%20Utility%20Plant","John%20Evans%20Alumni%20Center","Norris%20University%20Center","Shakespeare%20Garden","Allison%20Hall","Andersen%20Hall","Walter%20Annenberg%20Hall","Annie%20May%20Swift%20Hall","Ayers%20College%20of%20Commerce%20&%20Industry","Brentano%20Hall","Canterbury%20House","Catalysis%20Center","Chambers%20Hall","Chase%20Building","College%20of%20Cultural%20&%20Community%20Studies","Cook%20Hall","CRESAP%20Laboratory","Crowe%20Hall","Deering%20Meadow","Donald%20P.%20Jacobs%20Center","Engelhart%20Hall","%20House","The%20Family%20Institute%20at%20Northwestern%20University","Fisk%20Hall","Ford%20Motor%20Company%20Engineering%20Design%20Center","The%20Foster%20Walker%20Complex","Frances%20Searle%20Building","Harris%20Hall","Hogan%20Building","The%20Illinois%20Technology%20Enterprise%20Center","James%20L.%20Allen%20Center","John%20J.%20Louis%20Hall","Kresge%20Hall","Locy%20Hall","Lunt%20Hall","McManus%20Living%20Learning%20Center","Pancoe%20Evanston%20Northwestern%20Healthcare%20Life%20Sciences%20Pavilion","Parkes%20Hall","Rebecca%20Crown%20Center","Ryan%20Hall","Scott%20Hall","Searle%20Hall","Shanley%20Hall","Swift%20Hall","The%20McCormick%20Tribune%20Center","Abbott%20Hall","Arthur%20Rubloff%20Building","Feinberg%20Pavilion","Galter%20Pavilion","Health%20Sciences%20Building","Heating%20Plant","Jesse%20Brown%20VA%20Medical%20Center","Lake%20Shore%20Center","Levy%20Mayer%20Hall","McGaw%20Pavilion","Medical%20Science%20Building","Montgomery%20Ward%20Memorial%20Building","Morton%20Medical%20Research%20Building","Old%20Prentice%20Women's%20Hospital","Olson%20Pavilion","Prentice%20Women's%20Hospital%20and%20Maternity%20Center","Rehabilitation%20Institute%20of%20Chicago","Robert%20McCormick%20Hall","Searle%20Medical%20Research%20Building","Tarry%20Research%20&%20Education%20Building","The%20Robert%20H.%20Lurie%20Medical%20Research%20Center%20of%20Northwestern%20University","Wesley%20Pavilion","Wieboldt%20Hall","Worcester%20House"]
    keywords = list_of_building_names + ['Northwestern', 'NU', 'Wildcats', 'Wild', 'Ryan%20Auditorium']
    for key in keywords:
        SearchFbEvents(key)




def twitter(keyword):
    '''
    ckey = 'EyfkxkKOhm2UVVJxktfEC2rgp'
    csecret = 'V1JmyelPplrMSlf6g6iveJuKt0zP8mslAiS46oXl3UfzfGOQeN'
    atoken = '2900903370-OwZX1XZ2UgM3W4AraPqwaDnSc6nhr4MOg2VfBjz'
    asecret = '4orCMgKNmjQWOdRqE7OKtwAnUAZdl6a6oQ9hhATyi00Jn'
    '''
    ckey = 'lPYJc0qqrqRNkK5z4dqMAt1PA'
    csecret = 'WOJ7qSEFVNHyUynjfIKzCybSTZ6UrzMPuYZobkeeJ3PZe8dRcs'
    atoken = '1608194599-EnWHf0Q97PZe8kqoVr1yrPWgBGE1sBJUXYpZqRu'
    asecret = 'PIns8dfSGjHXhbLwET5c3S29NsuMkN3SvGxHFFmP26cdF'
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)

    results = api.search(q=keyword,count=100)
    if isRecent(results):
        return_list=[[unicode(result.id).encode('utf8'),unicode(result.author.name).encode('utf8'),unicode(result.text).encode('utf8'),unicode(str(result.created_at)).encode('utf8'),unicode(result.retweet_count).encode('utf8'), unicode(result.entities.get('media',[{}])[-1].get('media_url',None)).encode('utf8')] for result in results]
        return return_list
    else:
        return []

def keywordCleaning(input):
    import re
    words = input.split()
    return_value=""
    for word in words:
        word=word.lower()
        word= re.sub("[^A-Za-z]", "", word)
        if word=="nu" or word=="wildcats":
                    return_value+="northwestern "
        else:
            if len(word)>2:
                if word!="college" and word!="university" and word!="evanston" and word!="for" and word!="the" and word!="present" and word!="presents" and word!="and" and word!="vs" and word!="at" and word!="of" and word!="by" and word!="from" and word!="to" and word!="in":
                    return_value+=word+" "
    return return_value
def isRecent(input): #input is list of tweets
    import datetime
    sum=0
    for result in input:
        if result.created_at>(datetime.datetime.now()-datetime.timedelta(days=1)):
            sum+=1
    return sum>=0.33*len(input)


def FetchTweets(events):
    return_list=[]
    for event in events:
        tweets_list=twitter(keywordCleaning(event.name))
        if(tweets_list!=[]):
            for tweet in tweets_list:
                try:
                    t = Tweet.objects.get(id=tweet[0])
                    t.pic_url = tweet[-1]
                except ObjectDoesNotExist:
                    tw = Tweet(id=tweet[0], author=tweet[1], text=tweet[2],
                                  pub_date=datetime.datetime.strptime(tweet[3],"%Y-%m-%d %H:%M:%S"),
                                  num_retweet=tweet[4], event=event, pic_url=tweet[-1])
                    try:
                        t = Tweet.objects.get(text=tweet[2], num_retweet=tweet[4])
                        if (str(t.pub_date) < str(tw.pub_date)):
                            t.delete()
                            tw.save()
                    except ObjectDoesNotExist:
                        tw.save()
            #return_list.append({ 'tweets':tweets_list})
    return return_list



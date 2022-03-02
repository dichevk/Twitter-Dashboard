from eca import *
import eca.http
import json
from eca.generators import start_offline_tweets
import datetime
import textwrap
import pprint
import re
import datetime
def add_request_handlers(httpd):
    # use the library content from the template_static dir instead of our own
    # this is a bit finicky, since execution now depends on a proper working directory.
    httpd.add_content('/lib/', 'template_static/lib')
    httpd.add_content('/style/', 'template_static/style')

count =0.01
@event ('init')
def setup(ctx, e):
    # start the offline tweet stream
    start_offline_tweets('xfactor.txt', 'chirp', time_factor=2000)
    ctx.words = {}
    ctx.count =0
    fire('intence',{'previous':0.0})
def split_take(list0):
    
    x=list0.split()
    unwanted=[]
    i=0
    while i<=len(x):
        if i==3 or i==4:
            unwanted.append(x[i])
        i=i+1
        
    item_list=x
    item_list=[e for e in item_list if e not in unwanted]
    return item_list
@event ('chirp')
def tweet(ctx,e):
    tweet = e.data
    global count
    count +=1
    emit('chirp', tweet)
    
@event('cou')
def tweetcount(ctx,e):
    tweet = e.data
    ctx.count +=1
    emit('cou',{
        'action':'add',
        'value':ctx.count
    })

@event('intence')
def values(ctx,e):
   fire('intence', data=None, delay=1)
   global count
   emit('gr',{
        'action':'add',
        'value':count
    })
   count=0.01
   

        
    

    
    #emit('chirp', {
         #'text': json.dumps(tweet['text']),
         
    #})
    #for w in words(tweet['place']):
    #emit('chirp', {
        #'text': json.dumps(tweet['place']['country']),
    
    #})
    
    #emit('chirp', {
        #'text':split_take(tweet['created_at']),
    #})
    






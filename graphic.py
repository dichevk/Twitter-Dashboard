from eca import *
import eca.http
import json
from eca.generators import start_offline_tweets
import datetime
import textwrap
import pprint
import re
def add_request_handlers(httpd):
    # use the library content from the template_static dir instead of our own
    # this is a bit finicky, since execution now depends on a proper working directory.
    httpd.add_content('/lib/', 'template_static/lib')
    httpd.add_content('/style/', 'template_static/style')
@event ('init')
def setup(ctx, e):
    # start the offline tweet stream
    start_offline_tweets('xfactor.txt', 'tweet', time_factor=900)
    ctx.count =0
    fire('tweet',{'previous':0.0})

@event('tweet')
def generatetweet(ctx,e):
    tweet=e.data
    ctx.count +=1
    emit('tweet',{
        'action':'add',
        'value':tweet
    })
    fire('tweet',tweet,delay=None)
    

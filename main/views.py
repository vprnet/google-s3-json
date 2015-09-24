import os
import time
from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL
from sheet import get_google_sheet

@app.route('/')
def index():
    os.environ['TZ'] = 'US/Eastern'
    time.tzset()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    sheets = get_google_sheet()
    stories = []
    if len(sheets['vpr_news'])>0:
        for index, story in enumerate(sheets['vpr_news']):
    	    this_story = {}
    	    this_story['link'] = story['Link']
    	    this_story['story_id'] = story['Story ID']
    	    stories.append(this_story)        

    callout = {}
    callout['uri'] = sheets['callout'][0]['URI']
    callout['text'] = sheets['callout'][0]['Text']

    billboard = {}
    billboard['story_id'] = sheets['billboard'][0]['Story ID']
    billboard['title'] = sheets['billboard'][0]['Title']
    billboard['text'] = sheets['billboard'][0]['Text']
    billboard['link'] = sheets['billboard'][0]['Link']
    billboard['facebook'] = sheets['billboard'][0]['Facebook']
    billboard['twitter'] = sheets['billboard'][0]['Twitter']
    billboard['email'] = sheets['billboard'][0]['Email']
    billboard['phone'] = sheets['billboard'][0]['Phone']
	
    return render_template('vpr-homepage-app.json',
        timestamp=timestamp,
        stories=stories,
        callout=callout,
        billboard=billboard
        )

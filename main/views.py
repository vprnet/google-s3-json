import os
import time
import json
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
    	    this_story['link'] = json.dumps(story['Link'])
    	    if story['Story ID']=='':
        	    this_story['story_id']=0
    	    else:
    	        this_story['story_id'] = story['Story ID']
    	    stories.append(this_story)        

    callout = {}
    callout['uri'] = sheets['callout'][0]['URI']
    callout['text'] = json.dumps(sheets['callout'][0]['Text'])

    billboard = {}
    if sheets['billboard'][0]['Story ID']=='':
        billboard['story_id']=0
    else:
        billboard['story_id'] = sheets['billboard'][0]['Story ID']
    billboard['title'] = json.dumps(sheets['billboard'][0]['Title'])
    billboard['text'] = json.dumps(sheets['billboard'][0]['Text'])
    billboard['link'] = json.dumps(sheets['billboard'][0]['Link'])
    billboard['facebook'] = json.dumps(sheets['billboard'][0]['Facebook'])
    billboard['twitter'] = json.dumps(sheets['billboard'][0]['Twitter'])
    billboard['email'] = json.dumps(sheets['billboard'][0]['Email'])
    billboard['phone'] = json.dumps(sheets['billboard'][0]['Phone'])
	
    return render_template('vpr-homepage-app.json',
        timestamp=timestamp,
        stories=stories,
        callout=callout,
        billboard=billboard
        )

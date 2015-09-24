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
    sheet = get_google_sheet()
    stories = []
    if len(sheet)>0:
        for index, story in enumerate(sheet):
    	    this_story = {}
    	    this_story['link'] = story['Link']
    	    this_story['story_id'] = story['Story ID']
    	    stories.append(this_story)        

    return render_template('vpr-homepage-app.json',timestamp=timestamp,stories=stories)

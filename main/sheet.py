import os
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

def get_google_sheet():
    dir = os.path.dirname(os.path.realpath(__file__))
    json_key = json.load(open(dir +'/access.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key["client_email"], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open("VPR Homepage App")
    vpr_news = spreadsheet.get_worksheet(0)
    callout = spreadsheet.get_worksheet(1)
    billboard = spreadsheet.get_worksheet(2)
    sheets = {}
    sheets['vpr_news'] = vpr_news.get_all_records()
    sheets['callout'] = callout.get_all_records()
    sheets['billboard'] = billboard.get_all_records()

    return sheets
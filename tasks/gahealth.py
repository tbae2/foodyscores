#! python3
import requests
import sys






## script file that holds the tasks to scrape the ga health dept data 
## processes the dumped csv to upload into database
## pull data, process data, 
## mulltiple ways to check idempotency by run. use Id that is returned by health dept api to check for changes
## not the primary key, foreign key. 

def grabHealthScores():
    base_url = 'https://ga.healthinspections.us/stateofgeorgia/API/index.cfm/search/%7B%22city%22:%22TUFSSUVUVEE=%22,%22keyword%22:%22%22%7D/'

    pageCount = 0
    healthScoreHolder = []
    print('test test test')

    # while True:
    healthReq = requests.get("%s%s" % (base_url,pageCount))
    print(str(healthReq.status_code))

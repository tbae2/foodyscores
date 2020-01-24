#! python3
import requests
import sys
import json





## script file that holds the tasks to scrape the ga health dept data 
## processes the dumped csv to upload into database
## pull data, process data, 
## mulltiple ways to check idempotency by run. use Id that is returned by health dept api to check for changes
## not the primary key, foreign key. 

class restaurant():
    def __init__(self):
        self.name = restaurantName
        self.gaHealthScore = healthScore
        self.yelpScore = 0
    pass

class yelpInfo():
    def __init__(self,**kwargs):
        self.score = 0


def grabHealthScores():
    print('grabbing url')
    base_url = 'https://ga.healthinspections.us/stateofgeorgia/API/index.cfm/search/%7B%22city%22:%22TUFSSUVUVEE=%22,%22keyword%22:%22%22%7D/'
    print(base_url)
    pageCount = 0
    maxPageCount = 3
    healthScoreHolder = []
    noMoreData = False
    storeFile = open("testfile.csv","wt")
    print('test test test')

    # while True:
    # while noMoreData == False:
    while pageCount < maxPageCount:
        healthReq = requests.get("%s%s" % (base_url,pageCount))
        if len(healthReq.json()) > 0:
            healthScoreHolder += healthReq.json()
            pageCount += 1
        else:
            noMoreData = True
        
        
        print(str(healthReq.status_code))
    print(str(healthScoreHolder))
    # storeFile.write(healthScoreHolder)
    json.dump(healthScoreHolder,storeFile)
    storeFile.close()
    
if __name__ == "__main__":
    grabHealthScores()
#! python3
import requests
import sys
import json
import datetime
import os




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
    # ga department of health api that stores all the health reports for food establishments 
    base_url = 'https://ga.healthinspections.us/stateofgeorgia/API/index.cfm/search/%7B%22city%22:%22TUFSSUVUVEE=%22,%22keyword%22:%22%22%7D/'
    print(base_url)
    pageCount = 0
    currentDate = datetime.date.today()
    # maxPageCount = 3
    healthScoreHolder = []
    noMoreData = False
    storeFile = open(f"testfile{currentDate}.csv","wt")
    storePath = storeFile.name
    print(os.path.realpath(storePath))
    # while True:
    # while pageCount < maxPageCount:
    # loop through requests for given city url until the response is blank meaning no more data to return
    while noMoreData == False:
        try:    
            healthReq = requests.get("%s%s" % (base_url,pageCount))
            if len(healthReq.json()) > 0:
                healthScoreHolder += healthReq.json()
                pageCount += 1
                print(str(pageCount))
            else:
                noMoreData = True
        except Exception as e:
            print(healthReq.text)
            print(healthReq.status_code)
            raise e
        
        
    # print(str(healthReq.status_code))
    # print(str(healthScoreHolder))
    # storeFile.write(healthScoreHolder)
    json.dump(healthScoreHolder,storeFile)
    storeFile.close()
    return storePath
    
if __name__ == "__main__":
    grabHealthScores()
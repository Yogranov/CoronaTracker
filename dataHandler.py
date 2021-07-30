import json
import datetime
import post

def getYesterdayDatetime():
    with open('data.json') as f:
        data = json.load(f)
    return datetime.datetime.strptime(data['yesterday']['datetime'], '%Y-%m-%d %H:%M:%S')

def getYesterdayAmount():
    with open('data.json') as f:
        data = json.load(f)
    return data['yesterday']['amount']

def getTodayDatetime():
    with open('data.json') as f:
        data = json.load(f)
    return datetime.datetime.strptime(data['today']['datetime'], '%Y-%m-%d %H:%M:%S')

def getTodayAmount():
    with open('data.json') as f:
        data = json.load(f)
    return data['today']['amount']

def getTodayDiagnosis():
    with open('data.json') as f:
        data = json.load(f)
    return data['today']['diagnosis']

def getYesterdayDiagnosis():
    with open('data.json') as f:
        data = json.load(f)
    return data['yesterday']['diagnosis']


yesterdayDatetime = getYesterdayDatetime()
yesterdayAmount = getYesterdayAmount()

todayDatetime = getTodayDatetime()
todayAmount = getTodayAmount()
todayDiagnosis = getTodayDiagnosis()

def checkAndStore(lastUpdate, amount):
    with open('data.json') as f:
        data = json.load(f)

    if lastUpdate.day == todayDatetime.day:
        data['today']['datetime'] = lastUpdate.strftime('%Y-%m-%d %H:%M:%S')
        data['today']['amount'] = amount
        data['today']['diagnosis'] = post.getCurrentDiagnosis()
        
    else:
        data['yesterday']['datetime'] = todayDatetime.strftime('%Y-%m-%d %H:%M:%S')
        data['yesterday']['amount'] = todayAmount
        data['yesterday']['diagnosis'] = todayDiagnosis


        data['today']['datetime'] = lastUpdate.strftime('%Y-%m-%d %H:%M:%S')
        data['today']['amount'] = amount
        data['today']['diagnosis'] = post.getCurrentDiagnosis()

    with open('data.json', 'w') as f:
        json.dump(data, f)
    
    #return (amount - todayAmount), (todayDatetime)

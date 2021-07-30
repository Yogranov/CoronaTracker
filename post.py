import requests
import json
import datetime

url = "https://datadashboardapi.health.gov.il/api/queries/_batch"

raw_data = '{"requests":[{"id":"0","queryName":"lastUpdate","single":true,"parameters":{}},{"id":"1","queryName":"infectedPerDate","single":false,"parameters":{}},{"id":"2","queryName":"updatedPatientsOverallStatus","single":false,"parameters":{}},{"id":"3","queryName":"sickPerDateTwoDays","single":false,"parameters":{}},{"id":"4","queryName":"sickPerLocation","single":false,"parameters":{}},{"id":"5","queryName":"patientsPerDate","single":false,"parameters":{}},{"id":"6","queryName":"deadPatientsPerDate","single":false,"parameters":{}},{"id":"7","queryName":"recoveredPerDay","single":false,"parameters":{}},{"id":"8","queryName":"testResultsPerDate","single":false,"parameters":{}},{"id":"9","queryName":"infectedPerDate","single":false,"parameters":{}},{"id":"10","queryName":"patientsPerDate","single":false,"parameters":{}},{"id":"11","queryName":"doublingRate","single":false,"parameters":{}},{"id":"12","queryName":"infectedByAgeAndGenderPublic","single":false,"parameters":{"ageSections":[0,10,20,30,40,50,60,70,80,90]}},{"id":"13","queryName":"isolatedDoctorsAndNurses","single":true,"parameters":{}},{"id":"14","queryName":"testResultsPerDate","single":false,"parameters":{}},{"id":"15","queryName":"contagionDataPerCityPublic","single":false,"parameters":{}},{"id":"16","queryName":"hospitalStatus","single":false,"parameters":{}}]}'
header = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6',
    'Content-Type': 'application/json',
    'Host': 'datadashboardapi.health.gov.il',
    'Origin': 'https://datadashboard.health.gov.il',
    'Referer': 'https://datadashboard.health.gov.il/COVID-19/?utm_source=go.gov.il&utm_medium=referral',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Content-Length': '1337'

}
# getting data
respone = requests.post(url, data=raw_data, headers=header)
json = json.loads(respone.content)

# getting last update timestamp
lastUpdate = json[0]['data']['lastUpdate']
dateParse = lastUpdate[:-5]
dateParse = dateParse[:10] + ' ' + dateParse[-8:]

# final last update time
lastUpdateDatetime = datetime.datetime.strptime(dateParse, '%Y-%m-%d %H:%M:%S')
lastUpdateDatetime = lastUpdateDatetime.replace(hour=lastUpdateDatetime.hour+3)


def getLastUpdate():
    return lastUpdateDatetime


def getCurrentAmount():
    amountToday = 0
    amountYesterday = 0
    for data in json[1]['data']:
        amountToday += data['amount']

    return amountToday

def getCurrentDiagnosis():
    return json[8]['data'][-1]["amount"]

def getYesterdayDiagnosis():
    return json[8]['data'][-2]["amount"]
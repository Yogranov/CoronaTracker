import post
import dataHandler
import datetime
import notyHandler

lastUpdate = post.getLastUpdate()
todayDatetime = dataHandler.getTodayDatetime()


if(todayDatetime != lastUpdate):

    currentAmount = post.getCurrentAmount()
    dataHandler.checkAndStore(lastUpdate, currentAmount)

    diffrenceDiagnosis = post.getYesterdayDiagnosis() - dataHandler.getYesterdayDiagnosis()
    realDiagnosis = post.getCurrentDiagnosis() + diffrenceDiagnosis
    realAmount = currentAmount - dataHandler.getYesterdayAmount()
    positivePercent =  ("{:.2f}".format((realAmount / realDiagnosis * 100)) + '%')


    notyHandler.sendEmail(currentAmount - dataHandler.getYesterdayAmount(), dataHandler.getYesterdayDatetime(), positivePercent)
    notyHandler.discordMessage(currentAmount - dataHandler.getYesterdayAmount(), dataHandler.getYesterdayDatetime(), positivePercent)
    print("change detected!")

else:
    print("everything normal!")


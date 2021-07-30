import smtplib, ssl
import emailDetails
import codecs
import post
from email.mime.text import MIMEText
import requests

def sendEmail(amount, newTime, positivePercent):
    try:

        with open('email.html', 'r', encoding='utf-8') as f:
            html = f.read()
        
        html = html.replace('$yesterday$', newTime.strftime('%H:%M %d/%m/%Y'))
        html = html.replace('$lastUpdate$', post.getLastUpdate().strftime('%H:%M %d/%m/%Y'))
        html = html.replace('$positivePercent$', positivePercent)
        html = html.replace('$newCases$', str(amount))

        to = "youremail@gmail.com"

        msg = MIMEText(html, 'html', 'utf-8')
        msg['Subject'] = 'Corona Update'
        msg['From'] = f"Corona Update <{emailDetails.sender}>"
        msg['To'] = to

        server = smtplib.SMTP('mail.yourdomain.co.il', 587)
        server.ehlo()
        server.starttls()
        server.login(emailDetails.sender, emailDetails.password)
        server.sendmail(emailDetails.sender, to, msg.as_string())

    except:
        print ('Something went wrong...')

def discordMessage(amount, newTime, positivePercent):
    url = "https://discordapp.com/api/webhooks/" + "TOKEN"
    img = "https://image.flaticon.com/icons/png/512/2750/2750762.png"
    name = "Corona Bot"

    yesterdayDate = newTime.strftime('%H:%M %d/%m/%Y')
    currentDate = post.getLastUpdate().strftime('%H:%M %d/%m/%Y')

    content = f"""
        ----------------------------------------------
        חולים שנוספו היום: {str(amount)}
        אחוז חיוביים: {positivePercent}
        ```
        מתאריך {yesterdayDate}
        ועד תאריך {currentDate}
        ```
        ----------------------------------------------
        """

    data = {
        'username': name,
        'avatar_url': img,
        'content': content
    }

    requests.post(url, data=data)
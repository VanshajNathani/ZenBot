import time
import webbrowser
import csv
from wit import Wit
import csv
import wolframalpha
import smtplib

app_id = 'LJ8JG9-PU2K6GV5XU'
client1 = wolframalpha.Client(app_id)
client = Wit(access_token="YTKQJEF5P3DITHLT3TYGZVYYPVEPELHT")

def setReminder(idAddress,subject,data):

    # set reminder for subject on date to emailAddress
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = "zenbot2020covid@gmail.com"
    password = "acszxkxrjqngwclb"
    smtp_object.login(email, password)

    from_address = email
    to_address = idAddress
    subject = subject
    message = "Hello dear,\n\tKinda reminder for the event {} on date {}\nThanks\nZenBot".format(subject,data)
    msg = "Subject: " + subject + '\n' + message
    smtp_object.sendmail(from_address, to_address, msg)
    print(to_address)





def checkWeather(loc):
    query1 = "weather" + loc
    # res = client1.query(query1)
    # answer = next(res.results).text
    answer = callAPI(query1)
    answer = list(answer.split("\n"))
    finalAnswer = ""
    for i in answer:
        finalAnswer = finalAnswer + i.capitalize() + "\n"
    return finalAnswer


def checkSpreadsheet(entity):
    fp = "E:\\Python\\ChatBot\\Final\\ZenBotSpreadSheet - Sheet1.csv"
    finalAnswer = ""
    with open(fp, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (entity in row):
                for i in range(1, len(row)):
                    finalAnswer = finalAnswer + row[i] +"\n"
                    # print(row[i])
    return finalAnswer


def callAPI(n):
    try:
        app_id = 'LJ8JG9-PU2K6GV5XU'
        client1 = wolframalpha.Client(app_id)
        res = client1.query(n)
        answer = next(res.results).text
        return (answer)
    except:
        return None


def getTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return ("Current time is {}").format(current_time)

def body(n):
    intent = ""
    entity = ""
    loc = ""
    res = ""
    answer = ""
    # url = "https://www.wolframalpha.com/input/?i=weather+"
    # print("> ",end='')

    # if(n.lower() == "quit"):
    #     break
    resp = client.message(n)
    try:
        intent = resp['intents'][0]['name']
    except:
        pass
    try:
        if("ss_" in intent):
            entity = resp['entities']
            for b in entity:
                if(b == "wit$location:location"):
                    pass
                else:
                    entity = entity[b][0]["role"]
        else:
            entity = resp['entities']
            b = list(entity.keys())[0]
            entity = entity[b][0]["role"]
    except:
        pass
    try:
        loc = (resp['entities']['wit$location:location'][0]['body'])
    except:
        pass


    if("ss_" in intent):
       return checkSpreadsheet(entity)
    elif("w_" in intent or intent == "wit$check_weather_condition"):
        return callAPI(n)
    elif(intent == "wit$get_time"):
       return getTime()
    elif(intent == "wit$check_weather_condition" or intent == "w_weather"):
        return checkWeather(loc)
    # elif intent == "":
    #     if()
    else:
        try:
            return callAPI(n)
        except:
            return None

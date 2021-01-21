import json
import requests
import time
import urllib
from bas import body
TOKEN = <your token here>
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
from bas import setReminder


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
        url = URL + "getUpdates?offset=68655168"
        js = get_json_from_url(url)
        return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_textchat = ("Hi", None)
    while True:

        text, chat = get_last_chat_id_and_text(get_updates())
        # text = "Is it hot at mandi?"
        answer = body(text)

        if (text, chat) != last_textchat:
            print(text)
            # if "set reminder" in text.lower():
            #     mylist = text.split(" ")
            #     set reminder for subject on date to email
            #     setReminder(mylist[-1],mylist[3],mylist[5])
            #     answer = "Email will be sent on the specified date and time"
            if answer == None:
                link = "https://google.com/search?q={}".format(text.replace(" ","%20"))
                answer = "Sorry, I couldn't understand your query.\nYou may try something else or check the link below.\n{}".format(link)


            answer = answer.replace("Wolfram|Alpha", "ZenBot")
            send_message(answer, chat)
            print(answer)
            last_textchat = (text, chat)
        time.sleep(0.1)

if __name__ == '__main__':
    main()

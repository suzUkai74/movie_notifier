import urllib.request, urllib.error
import os
from kinro import Kinro
from premium_saturday import PremiumSaturday

LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"

def handler(event, context):
    messages = []
    programs = [Kinro(), PremiumSaturday()]

    for program in programs:
        messages.append(program.message())
    messages = [message for message in messages if message]

    for message in messages:
        send(message)

def send(message):
    headers = {"Authorization": "Bearer %s" % os.environ['LINE_TOKEN']}
    payload = {"message": message}
    try:
        payload = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url=LINE_NOTIFY_URL,
            data=payload,
            method="POST",
            headers=headers
        )
        urllib.request.urlopen(req)
    except Exception as e:
        print ("Exception Error: ", e)

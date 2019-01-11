import urllib.request, urllib.error
import os
from bs4 import BeautifulSoup

LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"
KINRO_URL = "https://kinro.jointv.jp/lineup"

class Movie:

    def __init__(self, program_name, title, date):
        self.program_name = program_name
        self.title = title
        self.date = date

    def build_message(self):
        return "%s\n%s : %s" % (self.program_name, self.date, self.title)

def handler:
    movies = []
    html = urllib.request.urlopen(url=KINRO_URL)
    soup = BeautifulSoup(html, "html.parser")
    for lineup in soup.find(id="after_lineup").find_all('li'):
        movie = Movie("金曜ロードショー", lineup.find(class_="date").get_text(), lineup.find(class_="title").get_text())
        movies.append(movie)

    for movie in movies:
        send(movie.build_message())

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

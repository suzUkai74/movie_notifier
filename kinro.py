import urllib.request, urllib.error
import datetime
from program import Program
from bs4 import BeautifulSoup

class Kinro(Program):
    PROGRAM_NAME = "金曜ロードショー"
    URL = "https://kinro.jointv.jp/lineup"

    def is_exec_day(self):
        return datetime.date.today().weekday() == 4

    def scraping(self):
        html = urllib.request.urlopen(url=self.URL)
        soup = BeautifulSoup(html, "html.parser")
        lineups = soup.find(id="after_lineup").find_all('li', limit=2)
        self.current = lineups[0]
        self.next = lineups[1]

    def find_date(self, movie):
        return movie.find(class_="date").get_text().strip('放送')

    def find_title(self, movie):
        return movie.find(class_="title").get_text()

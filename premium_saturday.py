import urllib.request, urllib.error
import datetime
import re
from program import Program
from bs4 import BeautifulSoup

class PremiumSaturday(Program):
    PROGRAM_NAME = "土曜プレミアム"
    URL = "https://www.fujitv.co.jp/premium/"

    def is_exec_day(self):
        return datetime.date.today().weekday() == 5

    def scraping(self):
        html = urllib.request.urlopen(url=self.URL)
        soup = BeautifulSoup(html, "html.parser")
        lineups = soup.find(id="lineup").find_all('div', class_="programbox")
        lineups = [lineup for lineup in lineups if self.string_to_date(self.find_date(lineup)) > datetime.date.today()]
        self.current = lineups[0]
        self.next = lineups[1]

    def string_to_date(self, date):
        split_date = [int(s) for s in date.split('/')]
        today = datetime.date.today()
        year = today.year
        if today.month == 12 and split_date[0] == 1:
            year += 1
        date = datetime.date(year, split_date[0], split_date[1])
        return date

    def find_date(self, movie):
        pattern = '(\d+\/\d+).*'
        repatter = re.compile(pattern)
        result = repatter.match(movie.find('span').get_text())
        return result.group(1)

    def find_title(self, movie):
        return movie.find('p').get_text().strip(movie.find('span').get_text())

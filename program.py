import datetime

class Program:

    def message(self):
        if not self.is_exec_day():
            return None
        self.scraping()
        self.validate()
        return self.build_message()

    def is_exec_day(self):
        return True

    def scraping(self):
        self.current = None
        self.next = None

    def validate(self):
        current_date = self.string_to_date(self.find_date(self.current))
        if not current_date == datetime.date.today():
            self.next = self.current
            self.current = None

    def build_message(self):
        message = self.PROGRAM_NAME
        if self.current is not None:
            message += "\n%s" % (self.build_movie_sentence(self.current))
        if self.next is not None:
            message += "\n%s" % (self.build_movie_sentence(self.next))
        return message

    def build_movie_sentence(self, movie):
        date = self.string_to_date(self.find_date(movie))
        title = self.find_title(movie)
        return "%s : %s" % (self.normalize_date(date), self.normalize_title(title))

    def string_to_date(self, date):
        split_date = [int(s) for s in date.split('.')]
        date = datetime.date(split_date[0], split_date[1], split_date[2])
        return date

    def find_date(self, movie):
        return datetime.date.today().strftime("%Y.%m.%d")

    def normalize_date(self, date):
        return "%s放送" % (date.strftime("%Y.%m.%d"))

    def find_title(self, movie):
        return "タイトルなし"

    def normalize_title(self, title):
        return title


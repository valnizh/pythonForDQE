import datetime

class Publication:
    NAME = ""
    BODY_PROMPT = ""
    FOOTER_PROMPT = ""
    FOOTER_TPL = ""
    DEVIDER_SIZE = 30
    def __init__(self):
        self.header = self.NAME
        self.body = input(self.BODY_PROMPT)
        self.footer_input = input(self.FOOTER_PROMPT)

    def _create_footer(self, *args, **kwargs):
        self.footer = self.FOOTER_TPL.format(*args, **kwargs)

    def write_file(self, path):
        lines = [
            self.header.ljust(self.DEVIDER_SIZE, '-'),
            self.body,
            self.footer,
            ''.ljust(self.DEVIDER_SIZE, '-'),
            '\n'
        ]
        with open(path, 'a+') as f:
            f.write('\n'.join(lines))
            f.write('\n')


class News(Publication):
    NAME = "News"
    BODY_PROMPT = "What happened? "
    FOOTER_PROMPT = "Where happened? "
    FOOTER_TPL = "{}, {}"

    def __init__(self):
        super().__init__()
        prime_time = datetime.datetime.now().strftime('%d/%m/%Y %H.%M')
        self._create_footer(self.footer_input, prime_time)


class PrivateAdd(Publication):
    NAME = "Private Add"
    BODY_PROMPT = "What`s the add? "
    FOOTER_PROMPT = "Due to (dd/mm/yyyy): "
    FOOTER_TPL = "Actual until: {}, {} left"

    def __init__(self):
        super().__init__()
        time_left = self._get_time_left()
        self._create_footer(self.footer_input, time_left)

    def _get_time_left(self):
        current_date = datetime.datetime.now()
        deadline_date = datetime.datetime.strptime(self.footer_input, '%d/%m/%Y')
        delta = abs((deadline_date - current_date).days)
        if delta == 1:
            return '1 day'
        return f'{delta} days'


class Weather(Publication):
    NAME = "Weather"
    BODY_PROMPT = "What`s the weather(sunny/cloudy/rain? "
    FOOTER_PROMPT = "Temperature is: "
    FOOTER_TPL = "Temperature: {}, feels like {}"

    def __init__(self):
        super().__init__()
        feels = self._suggest_temperature()
        self._create_footer(self.footer_input, feels)

    def _suggest_temperature(self):
        if self.body == 'sunny':
            return int(self.footer_input) + 4
        elif self.body == 'rain':
            return int(self.footer_input) - 2
        return self.footer_input


def open_news_feed(path):
    while True:
        pub_type = input('''
        To add News print - 1
        To add Private Add print - 2
        To add Weather Forecast print - 3
        To close feed print - c
    
        I want to add = ''')
        if pub_type == '1':
            pub = News()
        elif pub_type == '2':
            pub = PrivateAdd()
        elif pub_type == '3':
            pub = Weather()
        elif pub_type == 'c':
            break
        else:
            print('Unknown publication type')
            continue
        pub.write_file(path)


path = input('What path to file? (E.g. newsfeed.txt) ')
open_news_feed(path)



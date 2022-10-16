import datetime

class Publication:
    BODY_PROMPT = ""
    FOOTER_PROMPT = ""
    FOOTER_TPL = ""
    def __init__(self):
        self.body = input(self.BODY_PROMPT)
        self.footer_input = input(self.FOOTER_PROMPT)

    def _create_footer(self, *args, **kwargs):
        self.footer = self.FOOTER_TPL.format(*args, **kwargs)

    def write_file(self):
        pass


class News(Publication):

    BODY_PROMPT = "What happened? "
    FOOTER_PROMPT = "Where happened? "
    FOOTER_TPL = "{}, {}"

    def __init__(self):
        super().__init__()
        prime_time = datetime.datetime.now().strftime('%d/%m/%Y %H.%M')
        self._create_footer(self.footer_input, prime_time)


class PrivateAdd(Publication):
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






#pub_type = input('''
#    To add News print - 1
#     To add Private Add print - 2
    # To add Weather Forecast print - 3
    #
    # I want to add = ''')


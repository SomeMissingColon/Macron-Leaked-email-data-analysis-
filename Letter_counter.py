from urllib.request import urlopen as uOpen
from bs4 import BeautifulSoup as soup
import csv, re, math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


EMAIL_ID = 2


# Out of classes cuz doesnt fit any heredity
def list_gen(index):
    list = []
    for i in range(index):
        list.append(0)
    return list


class DataAnalysis:
    def __init__(self, parsed_data, id_data=0):
        self.parsed_data = parsed_data
        self.id_data = id_data

    def grapher(self):
        plt.bar(range(len(self.y_data)), self.y_data)
        plt.xticks(range(len(self.y_data)), self.x_data, size='small')
        plt.xLabel = ('letters')
        plt.yLabel = ('occurrence')
        plt.title('distributions of letters Macron\'s leaked emails\nup to email id:' + str(self.id_data))
        plt.show()

    def letter_finder(self):
        letter_amount_list = list_gen(26)
        letter_list = list_gen(26)
        indexer = 0
        for letter_id in range(97, 123):
            letter = chr(letter_id)
            letter_amount = len(re.findall(r'[' + letter + ']', self.parsed_data))
            #############Comodity############
            letter_list[indexer] = letter
            letter_amount_list[indexer] = letter_amount_list[indexer] + letter_amount
            #############Comodity############
            self.x_data, self.y_data = letter_list, letter_amount_list

            indexer += 1
        return self.x_data, self.y_data

            # Function below is useless for now, will come in handy later #

    def database_manager(self):
        with open('emails.csv', "a", encoding='utf-8') as output_file:
            csv_app = csv.writer(output_file)
            csv_app.writerow(['email id:', '%d' % self.id_data])


class RequestManagement:
    def __init__(self, url=''):
        self.url = url

    def request_web(self):
        request = uOpen(self.url)
        html_file = request.read()
        return html_file
        # def geturl(email_id):
        #    url = ('https://wikileaks.org/macron-emails/emailid/%d' % (email_id))
        #    return url


class Parsing:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def extract_email(self):
        bigsoup = soup(self.raw_data, 'html.parser')
        email_html = bigsoup.find('div', {'class': "email-content"})
        email = email_html.text
        return email

def main(EMAIL_ID):
    url = ('https://wikileaks.org/macron-emails/emailid/%d' % EMAIL_ID)

    macron_emails_data_set = RequestManagement(url = url)
    raw_data = macron_emails_data_set.request_web()
    parsed_data = Parsing(raw_data = raw_data)

    data_analysis = DataAnalysis(parsed_data=parsed_data.extract_email(), id_data = EMAIL_ID)
    data_analysis.letter_finder()
    data_analysis.grapher()

for i in range (10000):
    main(EMAIL_ID)
    EMAIL_ID += 1

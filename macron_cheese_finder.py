from urllib.request import urlopen as uOpen
from bs4 import BeautifulSoup as soup
import csv


def geturl(email_id):
    url = ('https://wikileaks.org/macron-emails/emailid/%d' % (email_id))
    return url


def request_web(url):
    request = uOpen(url)
    html_file = request.read()
    return html_file


def parser_basic(html_file):
    bigsoup = soup(html_file, 'html.parser')
    email_html = bigsoup.find('div', {'class': "email-content"})
    email = email_html.text
    return email


def database_manager(email, email_id):
    with open('emails.csv', "a", encoding='utf-8') as output_file:
        csv_app = csv.writer(output_file)
        csv_app.writerow('email id: %d' % (email_id))
        csv_app.writerow('email :'  + email)



def cheese_finder(email, email_id):
    if email.find('fromage') != -1:
        database_manager(email, email_id)
        print('cheese Found!')
    else:
        print('cheese not found :(')


def main():
    email_id = 0
    for i in range(71848):
        print('looking thru email Id : %d' % (email_id))
        cheese_finder(parser_basic(request_web(geturl(email_id))), email_id)
        email_id += 1


main()


import json
import bs4
import requests
import time
from datetime import datetime
import re
import xlsxwriter
import random
import smtplib
from email.message import EmailMessage

# import fake_useragent
import csv

# smtp
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'meratex.brest@gmail.com'
EMAIL_HOST_PASSWORD = 'jiknwufuibvrbgfe'
EMAIL_PORT = 587


def sendmail(to='savosinvitali@gmail.com', message='Привет'):
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Вас приветствует парсер ТриС'
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = to
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.send_message(msg)
    server.quit()


def get_data(url, page_count, retry=5):
    # user_agent = fake_useragent.UserAgent(use_cache_server=False, verify_ssl=False).random
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    try:
        response = requests.get(url=url, headers=headers)
    except Exception as ex:
        time.sleep(random.randrange(2, 5))
        if retry:
            print(f"Повтор-{page_count}")
            return get_data(url, page_count, retry=(retry - 1))
        else:
            raise
    else:
        return response


def dump_to_xlsx(data):
    headers = (
        '№',
        'Сумма',
        'Срок окончания',
        'Заказчик',
        'Предмет закупки',
        'Ссылка'
    )
    with xlsxwriter.Workbook(f'Результат_за_{datetime.now().strftime("%d.%m.%Y_%H.%M.%S")}.xlsx') as workbook:
        xl = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True, 'font_size': 18, 'fg_color': '#74AC4C', 'color': '#FFFFFF'})
        text_wrap = workbook.add_format({'text_wrap': True, 'border': True})
        # cell_format = workbook.add_format({'valign': 'vcenter',
        #                                    'text_wrap': True,
        #                                    'border': 1})

        link_format = workbook.get_default_url_format()
        link_format.set_align('vcenter')
        link_format.set_border(True)
        link_format.set_text_wrap(True)

        xl.set_column('B:C', 12)
        xl.set_column('A:A', 4)
        xl.set_column('D:F', 50)

        for i, header in enumerate(headers):
            xl.write_string(0, i, header, cell_format=bold)
        for i, item in enumerate(data, start=1):
            xl.write_string(i, 0, str(i), cell_format=text_wrap)
            xl.write_string(i, 1, item['price'], cell_format=text_wrap)
            xl.write_string(i, 2, item['date'], cell_format=text_wrap)
            xl.write_string(i, 3, item['customer'], cell_format=text_wrap)
            xl.write_string(i, 4, item['descriptions'], cell_format=text_wrap)
            xl.write_url(i, 5, item['url'], link_format)


def find_word_an_text(word, text):
    pass


def get_source_html():
    # print("Если будет введена некоректная дата, тогда отсчет пойдет с текущей даты")
    # date = input('Введите дату (dd.mm.yyyy): ')
    # try:
    #     time.strptime(date, '%d.%m.%Y')
    #     current_datetime = date
    # except ValueError:
    #     current_datetime = datetime.now().date().strftime("%d.%m.%Y")
    url = 'https://rabota.by/search/vacancy?text=python&salary=&ored_clusters=true'
    # # user_agent = fake_useragent.UserAgent(use_cache_server=False, verify_ssl=False).random
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    response = requests.get(url=url, headers=headers)
   

    soup = bs4.BeautifulSoup(response.text, "lxml")
    # print(soup)

    try:
        total_page = int(soup.find_all("span", class_="pager-item-not-in-short-range")[-1].find("a", class_="bloko-button").find("span").text)
    except Exception as ex:
        total_page = 1
    result_list = []
    print("Всего страниц:", type(total_page), total_page)
    # with open("dist/words.txt", encoding='UTF-8') as file:
    #     read_words = [word.strip() for word in file.readlines() if len(word) > 1]

    # words = [word.strip() for word in read_words if not re.match('-', word)]
    # extend_word = [word.strip('-') for word in read_words if re.match('-', word)]

    # print("Выбранные слова: ", words)
    # print("Исключенные слова: ", extend_word)
    for x in range(0, total_page):
        print("Ожидание:", x, '/', total_page)
        url = f'https://rabota.by/search/vacancy?search_field=name&search_field=company_name&search_field=description&enable_snippets=false&text=&page={x}'
        response = get_data(url, x, retry=5)

        soup = bs4.BeautifulSoup(response.text, "lxml")
        # print(soup.find_all("td", class_="serp-item"))
        # Разбиваем страницу по одной ссылке
        for link in soup.find_all("div", class_="serp-item"):
            job_type = link.find("h3").find("span").text
            print('222', job_type)
        #     # Цикл нужных слов
        #     for word in words:
        #         # Получаем текс в котором искать
        #         text = link.find("a").text
        #         if re.search(word, text, re.IGNORECASE):
        #             extendet = True
        #             for ext in extend_word:
        #                 if re.search(ext, text, re.IGNORECASE):
        #                     extendet = False
        #                     break
        #             if extendet:
        #                 url = link.find("a").get("href")
        #                 result_list.append(
        #                             {
        #                                 "descriptions": text,
        #                                 "url": f"https://goszakupki.by{url}",
        #                                 "customer": link.text,
        #                                 "price": link.next_sibling.next_sibling.next_sibling.next_sibling.text,
        #                                 "date": link.next_sibling.next_sibling.next_sibling.text
        #                             }
        #                         )
        #             break


    # dump_to_xlsx(result_list)
    return "[INFO] Данные собраны успешно!"


if __name__ == '__main__':
    get_source_html()
    

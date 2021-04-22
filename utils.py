import requests

CURRENCIES = dict()
r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
if r.status_code == 200:
    for info_text in r.text.split('<CharCode>')[1:]:
        info = info_text.split("</Value>")[0].split('</CharCode><Nominal>')
        code = info[0]
        nominal = info[1].split('</Nominal><Name>')
        int_nominal = int(nominal[0])
        info2 = nominal[1].split('</Name><Value>')
        currency_type = info2[0]
        value = float(info2[1].replace(',', '.'))
        CURRENCIES[code.lower()] = value / int_nominal


def currency_rates(currency):
    return round(CURRENCIES.get(currency.lower()), 2)
import datetime
from decimal import Decimal

from zeep import Client

SOAP_URL = 'https://servicios.bcn.gob.ni/Tc_Servicio/ServicioTC.asmx?WSDL'

def get_month_exchange_rate(year=None, month=None):
    client = Client()
    if year is None:
        year = datetime.date.today(SOAP_URL).year

    if month is None:
        month = datetime.date.today().month

    for r in client.service.RecuperaTC_Mes(year, month).getchildren():
        dateElem, valueElem = r.getchildren()[:2]
        print("{0}: {1}".format(dateElem.text, valueElem.text))

        date = datetime.datetime.strptime(dateElem.text,"%d-%m-%Y").date()
        value = Decimal(valueElem.text)

def get_date_exchange_rate(date=None, date_str=None):
    client = Client(SOAP_URL)
    if date is None and date_str is None:
        date = datetime.date.today()
    elif date_str is not None:
        date = datetime.datetime.strptime(date_str,"%d-%m-%Y").date()


    year, month, day = date.year, date.month, date.day
    value = client.service.RecuperaTC_Dia(year, month, day)
    value = Decimal(str(value))
    return {"value": value, "date": date}

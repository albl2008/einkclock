import datetime
import requests

year = datetime.datetime.now().year

url = f'https://api.argentinadatos.com/v1/feriados/{year}'

response = requests.get(url)


holidays = {

    # cumpleaños
    datetime.date(year, 1, 3): "CF  Tinto   ",
    datetime.date(year, 1, 25): "CF  Cabe-Huevo",
    datetime.date(year, 2, 10): "CF  Ema   ",
    datetime.date(year, 3, 1): "CF  Gaby   ",
    datetime.date(year, 3, 7): "CF  Caco   ",
    datetime.date(year, 3, 11): "CF  Fede   ",
    datetime.date(year, 3, 29): "CF  Ojon   ",
    datetime.date(year, 4, 1): "CF  Mellis   ",
    datetime.date(year, 4, 12): "CF  Stefa   ",
    datetime.date(year, 4, 27): "CF  Nacho   ",
    datetime.date(year, 5, 1): "CF  Luci   ",
    datetime.date(year, 5, 2): "CF  Nicos  ",
    datetime.date(year, 5, 17): "CF  Mati  ",
    datetime.date(year, 5, 21): "CF  Nico H  ",
    datetime.date(year, 6, 28): "CF  Tati  ",
    datetime.date(year, 7, 20): "CF  Mari   ",
    datetime.date(year, 7, 26): "CF  Noe   ",
    datetime.date(year, 8, 12): "CF  Juan  ",
    datetime.date(year, 8, 21): "CF  Lucho  ",
    datetime.date(year, 8, 27): "CF  Cabeza  ",
    datetime.date(year, 9, 24): "CF  Bata   ",
    datetime.date(year, 9, 5): "CF  JM   ",
    datetime.date(year, 10, 26): "CF  Bruno  ",
    datetime.date(year, 12, 17): "CF  Vieja   ",
    datetime.date(year, 11, 21): "CF  Viejo   ",
   
}

if response.status_code == 200:
    feriados = response.json()
    for feriado in feriados:
        fecha = datetime.datetime.strptime(feriado['fecha'], "%Y-%m-%d").date()
        holidays[fecha] = feriado['nombre']
else:
    print("Error fetching holidays")






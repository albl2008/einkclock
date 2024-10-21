import datetime

year = datetime.datetime.now().year

holidays = {
    datetime.date(year, 1, 1): "Año Nuevo",
    datetime.date(year, 2, 12): "Carnaval",
    datetime.date(year, 2, 13): "Carnaval",
    datetime.date(year, 3, 24): "Memoria verdad y justicia",
    datetime.date(year, 4, 2): "Veterano Malvinas",
    datetime.date(year, 5, 1): "Trabajador",
    datetime.date(year, 5, 25): "Revolución de Mayo",
    datetime.date(year, 6, 20): "Belgrano Inmortal",
    datetime.date(year, 7, 9): "Independencia",
    datetime.date(year, 12, 8): "Religioso",
    datetime.date(year, 12, 25): "Navidad",

    # Feriados trasladables
    datetime.date(year, 6, 17): "Güemes Inmortal",
    datetime.date(year, 8, 17): "San Martin Inmortal",
    datetime.date(year, 10, 12): "Diversidad Cultural",
    datetime.date(year, 11, 20): "Soberanía Nacional",

    # Feriados puentes
    datetime.date(year, 4, 1): "Bridge",
    datetime.date(year, 6, 21): "Bridge",
    datetime.date(year, 10, 11): "Bridge",

    # Feriados regionales
    datetime.date(year, 7, 25): "Patrono Santiago",


    # cumpleaños
    datetime.date(year, 9, 24): "CF FC Bata   ",
    datetime.date(year, 9, 26): "Alerta 1",
    datetime.date(year, 9, 27): "FERIADO ",
}

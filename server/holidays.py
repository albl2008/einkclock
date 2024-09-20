import datetime

year = datetime.datetime.now().year

holidays = {
    datetime.date(year, 1, 1): "Año Nuevo",
    datetime.date(year, 2, 12): "Carnaval",
    datetime.date(year, 2, 13): "Carnaval",
    datetime.date(year, 3, 24): "Día Nacional de la Memoria por la Verdad y la Justicia",
    datetime.date(year, 4, 2): "Día del Veterano y de los Caídos en la Guerra de Malvinas",
    datetime.date(year, 5, 1): "Día del Trabajo",
    datetime.date(year, 5, 25): "Día de la Revolución de Mayo",
    datetime.date(year, 6, 20): "Paso a la Inmortalidad del General Manuel Belgrano",
    datetime.date(year, 7, 9): "Día de la Independencia",
    datetime.date(year, 12, 8): "Día de la Inmaculada Concepción de María",
    datetime.date(year, 12, 25): "Navidad",

    # Feriados trasladables
    datetime.date(year, 6, 17): "Paso a la Inmortalidad del General Don Martín Miguel de Güemes",
    datetime.date(year, 8, 17): "Paso a la Inmortalidad del General Don José de San Martín",
    datetime.date(year, 10, 12): "Día del Respeto a la Diversidad Cultural",
    datetime.date(year, 11, 20): "Día de la Soberanía Nacional",

    # Feriados puentes
    datetime.date(year, 4, 1): "Feriado puente turístico",
    datetime.date(year, 6, 21): "Feriado puente turístico",
    datetime.date(year, 10, 11): "Feriado puente turístico",

    # Feriados regionales
    datetime.date(year, 7, 25): "Patrono Santiago",


    # cumpleaños
    datetime.date(year, 9, 24): "CF FC Bata   ",
    datetime.date(year, 10, 26): "FERIADO 1",
    datetime.date(year, 10, 27): "FERIADO 2",
}

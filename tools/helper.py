import json
import os
def translate(day:str):
    """
    Translates the name of a day to danish or english depending on which language the word was in first.
    :param str day: The name of the day.
    """
    translaterFilePath = os.path.join(os.path.dirname(__file__), "translator.json")
    with open(translaterFilePath, "r") as f:
        translations = json.loads(f.read())
        if day not in translations:
            print("The day {} is not in the list of translations.\nDefaulting to \"mandag\"".format(day))
            day = "mandag"
    return translations[day]
def correcter(time:str):
    """
    Takes the current time and corrects it to the closest lecture time.
    :param str time: The current time.
    """
    if time >= "08:30" and time <= "08:45": # Lect 0
        return "08:30 - 08:45"
    if time >= "08:45" and time <= "09:30": # Lect 1
        return "08:45 - 09:30"
    if time >= "09:30" and time <= "09:50": # Lect 2
        return "09:30 - 09:50"
    if time >= "09:50" and time <= "10:35": # Lect 3
        return "09:50 - 10:35"
    if time >= "10:35" and time <= "10:45": # Lect 4
        return "10:35 - 10:45"
    if time >= "10:45" and time <= "11:30": # Lect 5
        return "10:45 - 11:30"
    if time >= "11:30" and time <= "12:15": # Lect 6
        return "11:30 - 12:15"
    if time >= "12:15" and time <= "13:00": # Lect 7
        return "12:15 - 13:00"
    if time >= "13:00" and time <= "13:15": # Lect 8
        return "13:00 - 13:15"
    if time >= "13:15" and time <= "14:00":
        return "13:15 - 14:00"
def ordinal(n):
    """
    Returns the ordinal number of a number.
    :param str/int n: The number.
    """
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return str(n) + suffix
def monthNumber(monthNum): 
    """
    Returns the name of a month.
    :param int/str monthNum: The number of the month.
    """
    if type(monthNum) not in [int,str]:
        raise TypeError("monthNum must be a string or an integer.")
    monthNum = str(monthNum)
    months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
    }
    return months[monthNum]
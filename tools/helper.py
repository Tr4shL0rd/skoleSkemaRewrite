import json
def translate(day:str):
    with open("tools/translator.json", "r") as f:
        translations = json.loads(f.read())
    return translations[day]
def correcter(time:str):
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
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return str(n) + suffix
def monthNumber(monthNum): 
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
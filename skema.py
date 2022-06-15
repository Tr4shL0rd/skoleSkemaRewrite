import json
import datetime
from sys import argv
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from tools.helper import ordinal
from tools.helper import translate 
from tools.helper import correcter
from tools.helper import monthNumber
from tools.helper import move
from tools.helper import clear

def main(day:int=None):
    clear() # Prepares the terminal for the program.
    paddings = {
        "horizontal": "━",
        "vertical": "┃",
        "connecterBot": "┻",
        "connecterTop": "┳",
        "rightSideBot": "┛",
        "leftSideBot": "┗",
        "leftSideTop": "┏",
        "rightSideTop": "┓",
        "lineSplitter": "─",
        "lineConnecter": "╂",
        "lineConnecterRight": "┨",
        "lineConnecterLeft": "┠",
        "misc": {
            "topTable":    "┏━━━━━━━━━━━━━┳━━━━━━━━━━━━┓",
            "bottomTable": "┗━━━━━━━━━━━━━┻━━━━━━━━━━━━┛",
        }
    }
    weekdays = {
        1: "mandag",
        2: "tirsdag",
        3: "onsdag",
        4: "torsdag",
        5: "fredag",
        6: "lørdag",
        0: "søndag"
    }
    daySpaces = {
        "monday":    " "*7,
        "tuesday":   " "*6,
        "wednesday": " "*4,
        "thursday":  " "*5,
        "friday":    " "*7,
        "saturday":  " "*7,
        "sunday":    " "*7
    }
    monthSpaces = {
        "January":   " "*4,
        "February":  " "*3,
        "March":     " "*6,
        "April":     " "*6,
        "May":       " "*8,
        "June":      " "*7,
        "July":      " "*7,
        "August":    " "*5,
        "September": " "*2,
        "October":   " "*4,
        "November":  " "*3,
        "December":  " "*3
    }
    lectureNames = {
        "MATEMATIK": "MATEMATIK  ",
        "DANSK":     "DANSK      ",
        "ENGELSK":   "ENGELSK    ",
        "IDRÆT":     "IDRÆT      ",
        "runde":     "runde      ",
        "pause":     "pause      ",
        "IU":        "IU         ",      
    }
    nonLectures = [
        "pause", 
        "runde"
    ]
    movePos = (25,40)
    formatting = False
    # Date Variables
    date      = datetime.datetime.now()
    dateYear  = date.year
    dateMonth = date.month
    dateDay   = date.day
    # Prettifying Dates
    day           = weekdays[day] if day else weekdays[datetime.datetime.now().weekday()] # if day is not specified, it will be the current day.
    betterDay     = f"{ordinal(dateDay)} of {monthNumber(dateMonth)}"
    currentTime   = str(datetime.datetime.now())[11:16]
    correctedTime = correcter(str(datetime.datetime.now())[11:16])
    
    
    if dateDay < 10:
        betterDay += " "
    if day in ["lørdag", "søndag"]:
        day = "mandag"
    if not formatting:
        print(f"┏{'━'*24}{'┓'}")
        print(f"┃{translate(day).title()} {currentTime} {daySpaces[translate(day)]}{' '*4}┃") # Day name and time
        print(f"┠{'─'*24}{'┨'}") # Line Splitter
        print(f"┃{betterDay}{monthSpaces[monthNumber(dateMonth)]}{dateYear} ┃") # Day number, month and year
        print(f"┗{'━'*24}{'┛'}")
        movePos = (25,40)
    else:
        print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━┓
┃{translate(day).title()} {currentTime} {daySpaces[translate(day)]}{' '*3}┃
┠───────────────────────┨
┃{betterDay}{monthSpaces[monthNumber(dateMonth)]}{dateYear}┃
┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
        movePos = (26,40)
    splitter = f"\n{paddings['lineConnecterLeft']}{paddings['lineSplitter']*13}{paddings['lineConnecter']}{paddings['lineSplitter']*12}{paddings['lineConnecterRight']}"
    with open("lectures.json", "r") as lectureFile:
        lectures = json.loads(lectureFile.read())
        currentLecture = ""
        #print(f"{paddings['leftSideTop']}{paddings['horizontal']*13}{paddings['connecterTop']}{paddings['horizontal']*12}{paddings['rightSideTop']}")
        print(paddings["misc"]["topTable"])
        for k,v in lectures[day].items():
            prettyK = f"{paddings['vertical']}{k}{paddings['vertical']}"
            if  v.strip() not in ["pause", "runde"]:
                # logic to check wether the lecture is entered in correctly
                if v != v.upper():          
                    v = v.upper()           
            if len(v) != 11:                
                v = f"{v}{' '*(11-len(v))}" 
            if v.strip() not in nonLectures:
                if k == correctedTime:
                    rprint(f"{prettyK} [cyan]{v}[/cyan]{paddings['vertical']}{splitter}")    
                    currentLecture = v
                    continue
                rprint(f"{prettyK} [blue]{v}[/blue]{paddings['vertical']}{splitter}")
            if v.strip() in nonLectures:
                if k == correctedTime:
                    rprint(f"{prettyK} [cyan]{v}[/cyan]{paddings['vertical']}{splitter}")    
                    currentLecture = v
                    continue
                rprint(f"{prettyK} [red]{v}[/red]{paddings['vertical']}{splitter}")
        # prevents the last print being a half cell 
        if k == "13:15 - 14:00":
            move(movePos)
            print(paddings["misc"]["bottomTable"])
        elif k == "12:15 - 13:00" and day == "fredag":
            move((21,40))
            print(paddings["misc"]["bottomTable"])
        #print(f"{paddings['leftSideBot']}{paddings['horizontal']*13}{paddings['connecterBot']}{paddings['horizontal']*12}{paddings['rightSideBot']}")
    return currentLecture 

colorCommands = ["-c", "--color","--colors", "c", "color", "colors"]
helpCommands  = ["-h", "--help", "h", "help"]
nextCommands  = ["-n", "--next", "n", "next"]
console = Console()
table = Table()
argv = list(map(lambda x: x.lower(), argv))
colorsUsed = {
    "cyan": "Nuværende Lektion",
    "blue": "Skole Lektioner",
    "red":  "Pauser",
}
commands = {
    "--help":   ("Shows this message",                  "skema.py --help"    ),
    "--color":  ("Shows the colors used in the output", "skema.py --color"   ),
    "--next n": ("Shows the lectures for the next day", "skema.py --next 1-5")
}
def Help():
    # Adding columns
    table.add_column("Command")
    table.add_column("Description")
    table.add_column("Usage")
    # Adding Rows
    for k,v in commands.items():
        table.add_row(f"{k}", f"{v[0]}", f"{v[1]}")
    
    console.print(table)

if len(argv) >= 2:
    if argv[1] in colorCommands:
        table.add_column("Color")
        table.add_column("Meaning")
        for k,v in colorsUsed.items():
            table.add_row(f"[{k}]{k.upper()}", f"[{k}]{v}[/{k}]")
        console.print(table)
    elif argv[1] in helpCommands:
        Help()
    elif argv[1] in nextCommands:
        if len(argv) == 3:
            if int(argv[2]) > 5 or int(argv[2]) < 1:
                rprint("[red]Error:[/red] The day must be between 1 and 5")
                exit()
            else:
                rprint("[red]Error:[/red] Please specify a day")
                Help()
            main(int(argv[2]))
    else:
        console.print(f"[red]Error:[/red] Command [red underline]\"{argv[1]}\"[/red underline] not found!")
        Help()
    exit()
main(None)

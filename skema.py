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
def main():
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
        "lineConnecterLeft": "┠"
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
    # Date Variables
    date      = datetime.datetime.now()
    dateYear  = date.year
    dateMonth = date.month
    dateDay   = date.day
    # Prettifying Dates
    day           = weekdays[datetime.datetime.now().weekday()]
    betterDay     = f"{ordinal(dateDay)} of {monthNumber(dateMonth)}"
    currentTime   = str(datetime.datetime.now())[11:16]
    correctedTime = correcter(str(datetime.datetime.now())[11:16])
    
    if dateDay < 10:
        betterDay += " "
    if day in ["lørdag", "søndag"]:
        day = "mandag"
    print(f"┏{'━'*24}{'┓'}")
    print(f"┃{translate(day).title()} {currentTime} {daySpaces[translate(day)]}{' '*4}┃") # Day name and time
    print(f"┠{'─'*24}{'┨'}") # Line Splitter
    print(f"┃{betterDay}{monthSpaces[monthNumber(dateMonth)]}{dateYear} ┃") # Day number, month and year
    print(f"┗{'━'*24}{'┛'}")
    
    splitter = f"\n{paddings['lineConnecterLeft']}{paddings['lineSplitter']*13}{paddings['lineConnecter']}{paddings['lineSplitter']*12}{paddings['lineConnecterRight']}"

    with open("lectures.json", "r") as lectureFile:
        lectures = json.loads(lectureFile.read())
        currentLecture = ""
        print(f"{paddings['leftSideTop']}{paddings['horizontal']*13}{paddings['connecterTop']}{paddings['horizontal']*12}{paddings['rightSideTop']}")
        for k,v in lectures[day].items():
            prettyK = f"{paddings['vertical']}{k}{paddings['vertical']}"

            if v.strip() not in ["pause","runde"]:
                if k == correctedTime:
                    rprint(f"{prettyK} [cyan]{v}[/cyan]{paddings['vertical']}{splitter}")    
                    currentLecture = v
                    continue
                rprint(f"{prettyK} [blue]{v}[/blue]{paddings['vertical']}{splitter}")
            
            if v.strip() in ["pause","runde"]:
                if k == correctedTime:
                    rprint(f"{prettyK} [cyan]{v}[/cyan]{paddings['vertical']}{splitter}")    
                    currentLecture = v
                    continue
                rprint(f"{prettyK} [red]{v}[/red]{paddings['vertical']}{splitter}")
        # prevents the last print being a half cell 
        if k == "13:15 - 14:00":
            move(25,40)
            print("┗━━━━━━━━━━━━━┻━━━━━━━━━━━━┛")
        #print(f"{paddings['leftSideBot']}{paddings['horizontal']*13}{paddings['connecterBot']}{paddings['horizontal']*12}{paddings['rightSideBot']}")
    return currentLecture 

colorCommands = ["-c", "--color","--colors", "c", "color", "colors"]
helpCommands  = ["-h", "--help", "h", "help"]
console = Console()
table = Table()
argv = list(map(lambda x: x.lower(), argv))
colorsUsed = {
    "cyan": "Nuværende Lektion",
    "blue": "Skole Lektioner",
    "red":  "Pauser",
}
commands = {
    "--help": "Shows this message",
    "--color": "Shows the colors used in the output",
}
def Help():
    table.add_column("Command")
    table.add_column("Description")
    for k,v in commands.items():
        table.add_row(f"{k}", f"{v}")
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
    else:
        console.print(f"Command [red underline]\"{argv[1]}\"[/red underline] not found!")
        Help()
    exit()
main()

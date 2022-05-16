import os
import json

data = {
    "ATL" : "Atlanta Hawks",
    "BOS" : "Boston Celtics",
    "BRK" : "Brooklyn Nets",
    "CHI" : "Chicago Bulls",
    "CHO" : "Charlotte Hornets",
    "CLE" : "Cleveland Cavaliers",
    "DAL" : "Dallas Mavericks",
    "DEN" : "Denver Nuggets",
    "DET" : "Detroit Pistons",
    "GSW" : "Golden State Warriors",
    "HOU" : "Houston Rockets",
    "IND" : "Indiana Pacers",
    "LAC" : "Los Angeles Clippers",
    "LAL" : "Los Angeles Lakers",
    "MEM" : "Memphis Grizzlies",
    "MIA" : "Miami Heat",
    "MIL" : "Milwaukee Bucks",
    "MIN" : "Minnesota Timberwolves",
    "NOP" : "New Orleans Pelicans",
    "NYK" : "New York Knicks",
    "OKC" : "Oklahoma City Thunder",
    "ORL" : "Orlando Magic",
    "PHI" : "Philadelphia 76ers",
    "PHO" : "Phoenix Suns",
    "POR" : "Portland Trail Blazers",
    "SAC" : "Sacramento Kings",
    "SAS" : "San Antonio Spurs",
    "TOR" : "Toronto Raptors",
    "UTA" : "Utah Jazz",
    "WAS" : "Washington Wizards"
}

reverse = {}
for d in data:
    reverse[data[d]] = d

full = {}

year = 2022
directory = f"games/{year}"
for filename in os.listdir(directory):
    if filename.endswith(".txt"): 

        code = filename[0:filename.index('.')]
        
        path = os.path.join(directory, filename)

        full[code] = {}

        with open(path) as file:
            for line in file:
                cols = line.split(',')

                opp_code = reverse[cols[0]]

                if opp_code not in full[code]:
                    full[code][opp_code] = []

                #print(path, code, opp_code, cols[1], cols[2])
                full[code][opp_code].append({'team': int(cols[1]), 'opp': int(cols[2])})


with open(f'games{year}.json', 'w') as fp:
    json.dump(full, fp,  indent=4)



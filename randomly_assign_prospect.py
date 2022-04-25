# Top 32 prospects according to this cbs site https://www.cbssports.com/nfl/draft/prospect-rankings/
# which was the first result from google for the search `top nfl draft prospects`
import random
from tabulate import tabulate

prospects = [
    'Aidan Hutchinson (1)',
    'Evan Neal (2)',
    'Ahmad Gardner (3)',
    'Kyle Hamilton (4)',
    'Derek Stingley Jr. (5)',
    'Kayvon Thibodeaux (6)',
    'Garrett Wilson (7)',
    'Charles Cross (8)',
    'Tyler Linderbaum (9)',
    'Ikem Ekwonu (10)',
    'Jameson Williams (11)',
    'Drake London (12)',
    'Travon Walker (13)',
    'Nakobe Dean (14)',
    'Treylon Burks (15)',
    'Andrew Booth Jr. (16)',
    'Jordan Davis (17)',
    'Daxton Hill (18)',
    'Jermaine Johnson II (19)',
    'Devin Lloyd (20)',
    'Bernhard Raimann (21)',
    'Trent McDuffie (22)',
    'Malik Willis (23)',
    'Boye Mafe (24)',
    'Roger McCreary (25)',
    'George Karlaftis (26)',
    'Kenyon Green (27)',
    'Devonte Wyatt (28)',
    'Chris Olave (29)',
    'Kenny Pickett (30)',
    'Lewis Cine (31)',
    'Zion Johnson (32)']

fantasy_finish_place = [
    "Weekend Warriors (Chris)",
    "Nard Dog (Andy)",
    "Judge Jeudy (Andrew)",
    "Crystal Cannon (Julian)",
    "The Freshmaker (Dan)",
    "Draft Error (Nate)",
    "Touchdown My Pants (Micah)",
    "Wants Moore Clarence (Matt)",
    "Wantz to win (Joe)",
    "theReplacements (Lance)",
    "Earthwake and Suhnami (Mike)",
    "Ravens Row (Kris)"
]

table_entries = []
random_prospects = random.sample(prospects, len(fantasy_finish_place))
for i, team in enumerate(fantasy_finish_place):
    prospect = random_prospects[i]
    table_entries.append([team, prospect])
# FTW 
#    for team in fantasy_finish_place:
#    if team == 'Weekend Warriors (Chris)':
#        prospect = 'Aidan Hutchinson (1)'
#        table_entries.append([team, prospect])
#    else:
#        prospect = random.sample(prospects[1:], 1)[0]
#        table_entries.append([team, prospect])
print(tabulate(table_entries, headers=["Team Name", "Prospect"]))

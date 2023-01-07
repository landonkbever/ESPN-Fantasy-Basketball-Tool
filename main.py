#ESPN Fantasy Basketball tool
#Used to take grown men's money

from espn_api.basketball import League
import datetime
global league
league = League(league_id=1330860437, year=2023, espn_s2='AEC2JFptBpZayXb6oywXx6ANqklaYZPAt03zUEx7Mc141AE6mYOcOSvnFr3CWhhGWuYIRThu1eYKb1kVLdNoKP4RSyLXqGJQR2eswKnhyySWRRkavf%2BakY6jgs0bcJHNPECxcvI3eUNYZTWpfpL9bBQEE4ytzQDDn%2FiqHq%2BKywWIXhqVNgKYWFKHguoOH6lbtqORRLer%2FbtEXJTSE9HyNbmm7U4%2BypY3%2F9A3FYr4eqiMc6%2BOEzlT7ubGXnnNKO%2FVRa1BR8VhuokgICHheMKaZV2P', swid='{2EA153B1-AE28-425A-832F-5BBD45F22D80}')

global myteam
myteam = league.teams[3] #prints Team(Who Invited The Kid)
global myroster
myroster = myteam.roster #prints list: Player(x),...
global leaguebox
leaguebox = league.box_scores() #prints [Box Score(Team(teamname) at Team(teamname)), ...]

today = datetime.date.today()
nbaweeks = {#if date is greater than week1 and less than or equal to week2, then date is in week2
    0:datetime.date(2022,10,16),
    1:datetime.date(2022,10,23),
    2:datetime.date(2022,10,30),
    3:datetime.date(2022,11,6),
    4:datetime.date(2022,11,13),
    5:datetime.date(2022,11,20),
    6:datetime.date(2022,11,27),
    7:datetime.date(2022,12,4),
    8:datetime.date(2022,12,11),
    9:datetime.date(2022,12,18),
    10:datetime.date(2022,12,25),
    11:datetime.date(2023,1,1),
    12:datetime.date(2023,1,8),
    13:datetime.date(2023,1,15),
    14:datetime.date(2023,1,22),
    15:datetime.date(2023,1,29),
    16:datetime.date(2023,2,5),
    17:datetime.date(2023,2,12),
    18:datetime.date(2023,2,26),
    19:datetime.date(2023,3,5),
    20:datetime.date(2023,3,12),
    21:datetime.date(2023,3,19),
    22:datetime.date(2023,3,26),
    23:datetime.date(2023,4,2),
    24:datetime.date(2023,4,9)
    }

def getweek(date=datetime.date.today()):
    for key,value in nbaweeks.items():
        if date > value and date <= nbaweeks[key+1]:
            return key+1

def getmatchupid(team):
    i = -1
    teambox = ''
    for matchup in leaguebox:
        i += 1
        if str(team) in str(matchup):
            teambox = i
            break
    return teambox

def showmatchup(matchupid):
    teamsplit = str(leaguebox[matchupid]).split(' at ')
    teamsplit[0] = teamsplit[0][15:-1]
    teamsplit[1] = teamsplit[1][5:-2]
    return teamsplit #returns ['team1', 'team2']

def showallmatchups():
    allmatchups = []
    for matchup in leaguebox:
        allmatchups.append(showmatchup())
    return allmatchups











def main():
    print('')#current matchup


#print(showmatchup(getmatchupid(myteam)))
#print(showallmatchups())

#for key,value in myroster[0].schedule.items():
    #print(f'{key}    {value}')


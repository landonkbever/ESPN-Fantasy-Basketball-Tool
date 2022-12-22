#ESPN Fantasy Basketball tool
#Used to take grown men's money

from espn_api.basketball import League
global league
league = League(league_id=1330860437, year=2023, espn_s2='AEC2JFptBpZayXb6oywXx6ANqklaYZPAt03zUEx7Mc141AE6mYOcOSvnFr3CWhhGWuYIRThu1eYKb1kVLdNoKP4RSyLXqGJQR2eswKnhyySWRRkavf%2BakY6jgs0bcJHNPECxcvI3eUNYZTWpfpL9bBQEE4ytzQDDn%2FiqHq%2BKywWIXhqVNgKYWFKHguoOH6lbtqORRLer%2FbtEXJTSE9HyNbmm7U4%2BypY3%2F9A3FYr4eqiMc6%2BOEzlT7ubGXnnNKO%2FVRa1BR8VhuokgICHheMKaZV2P', swid='{2EA153B1-AE28-425A-832F-5BBD45F22D80}')

global myteam
myteam = league.teams[3] #prints Team(Who Invited The Kid)
global myroster
myroster = myteam.roster #prints list: Player(x),...
global leaguebox
leaguebox = league.box_scores()

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

matchups = league.scoreboard(5)
print(matchups)

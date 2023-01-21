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
    '''Returns the week that a given date is within'''
    for key,value in nbaweeks.items():
        if date > value and date <= nbaweeks[key+1]:
            return key+1

def showmatchup(matchupid):
    '''Returns list of two teams facing each other'''
    teamsplit = str(leaguebox[matchupid]).split(' at ')
    teamsplit[0] = teamsplit[0][15:-1]
    teamsplit[1] = teamsplit[1][5:-2]
    return teamsplit #returns ['team1', 'team2']

def showallmatchups():
    '''Returns list of sublists of two teams facing each other'''
    allmatchups = []
    for i in range(5):
        allmatchups.append(showmatchup(i))
    return allmatchups

def playernumofgames(player, week=getweek()):
    '''Finds number of games for a player in a given week'''
    games = 0
    schedule = player.schedule.values()
    newgames = []
    playerdates = []
    for game in schedule:
        newgames.append(game)
    for game in newgames:
        for key, value in game.items():
            if key == 'date':
                playerdates.append(value)
    for date in playerdates:
        date = date.date()
        if getweek(date) == week:
            games += 1
    return games
    
def teamnumofgames(team, week=getweek()):
    '''Uses playernumofgames() to find a team's total game count of a given week'''
    teamgames = 0
    for player in team.roster:
        teamgames += playernumofgames(player, week)
    return teamgames

def standings():
    '''Returns list of strings, team records first and team name next'''
    stands = []
    for team in league.standings():
        stands.append(f'{team.wins}-{team.losses}-{team.ties} {team.team_name}')
    return stands

def statprojection():
    pass

def recent_activity(ttype='WAVIER', num=10):
    activities = []
    for activity in league.recent_activity(num, ttype):# msg_type inputs: 'FA', 'WAVIER', 'TRADED'
        activities.append(activity)
    return activities

def schedule(team):
    '''Returns full schedule of given team in a list of strings'''
    i = 1
    weeks = []
    for matchup in team.schedule:
        matchup = str(matchup)
        if ' - ' in matchup:
            matchupsplit = matchup.split(' - ')
            team1 = matchupsplit[0]
            team1 = team1[13:-5]
            #team1 = [team1, matchupsplit[0][-3:]]
            team2 = matchupsplit[1]
            team2 = team2[9:-2]
            #team2 = [team2, matchupsplit[1][:3]]
            week = 'Week ' + str(i) + ': ' + team1 + ' vs ' + team2
            i += 1
            weeks.append(week)
        elif '), ' in matchup:
            matchupsplit = matchup.split('), ')
            team1 = matchupsplit[0]
            team1 = team1[13:]
            team2 = matchupsplit[1]
            team2 = team2[5:-2]
            week = 'Week ' + str(i) + ': ' + team1 + ' vs ' + team2
            i += 1
            weeks.append(week)
    return weeks
            
#
#what to do about ties in schedule(team)
#








def main():
    choice = ''
    while choice != 10:
        print('Fantasy Basketball Tool for Who Invited The Kid')
        print(f'{schedule(myteam)[getweek() - 1]}\n')
        print('1) Matchup stats and projections')
        print('2) Show all matchups')
        print('3) Schedule')
        print('4) My games vs oppenents games')
        print('5) Recent league activity')
        print('6) Compare player stats')
        print('7) Standings')
        choice = int(input('Option: '))
        print('')

        if choice == 1:
            pass
        elif choice == 2:
            for match in showallmatchups():
                print(match[0] + ' vs ' + match[1])
            print('\n')
        elif choice == 3:
            #change to choose team
            for week in schedule(myteam):
                print(week)
            print('\n')
        elif choice == 4:
            #change to choose options
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
main()

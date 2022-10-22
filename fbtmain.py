#ESPN Fantasy Basketball tool
#Used to take grown men's money

from espn_api.basketball import League
league = League(league_id=1330860437, year=2023, espn_s2='AEC2JFptBpZayXb6oywXx6ANqklaYZPAt03zUEx7Mc141AE6mYOcOSvnFr3CWhhGWuYIRThu1eYKb1kVLdNoKP4RSyLXqGJQR2eswKnhyySWRRkavf%2BakY6jgs0bcJHNPECxcvI3eUNYZTWpfpL9bBQEE4ytzQDDn%2FiqHq%2BKywWIXhqVNgKYWFKHguoOH6lbtqORRLer%2FbtEXJTSE9HyNbmm7U4%2BypY3%2F9A3FYr4eqiMc6%2BOEzlT7ubGXnnNKO%2FVRa1BR8VhuokgICHheMKaZV2P', swid='{2EA153B1-AE28-425A-832F-5BBD45F22D80}')

myteam = league.teams[3]
myteam_avg_fgp = 0
myteam_avg_ftp = 0
myteam_avg_3pm = 0
myteam_avg_reb = 0
myteam_avg_ast = 0
myteam_avg_stl = 0
myteam_avg_blk = 0
myteam_avg_pts = 0

myteam_p_fgp = 0
myteam_p_ftp = 0
myteam_p_3pm = 0
myteam_p_reb = 0
myteam_p_ast = 0
myteam_p_stl = 0
myteam_p_blk = 0
myteam_p_pts = 0

oppteam_avg_fgp = 0
oppteam_avg_ftp = 0
oppteam_avg_3pm = 0
oppteam_avg_reb = 0
oppteam_avg_ast = 0
oppteam_avg_stl = 0
oppteam_avg_blk = 0
oppteam_avg_pts = 0

oppteam_p_fgp = 0
oppteam_p_ftp = 0
oppteam_p_3pm = 0
oppteam_p_reb = 0
oppteam_p_ast = 0
oppteam_p_stl = 0
oppteam_p_blk = 0
oppteam_p_pts = 0

'''
change to opproster
opp1 = myroster[0]
opp2 = myroster[1]
opp3 = myroster[2]
opp4 = myroster[3]
opp5 = myroster[4]
opp6 = myroster[5]
opp7 = myroster[6]
opp8 = myroster[7]
opp9 = myroster[8]
opp10 = myroster[9]
opp11 = myroster[10]
opp12 = myroster[11]
opp13 = myroster[12]
'''

boxs = league.box_scores()
while True:
    i = -1
    for box in boxs:
        i += 1
        if 'Team(Who invited The kid)' in str(box):
            boxidx = i
    break
mybox = boxs[boxidx]

myroster = myteam.roster
for player in myroster:
    pass

mp1 = myroster[0]
mp2 = myroster[1]
mp3 = myroster[2]
mp4 = myroster[3]
mp5 = myroster[4]
mp6 = myroster[5]
mp7 = myroster[6]
mp8 = myroster[7]
mp9 = myroster[8]
mp10 = myroster[9]
mp11 = myroster[10]
mp12 = myroster[11]
mp13 = myroster[12]
mypyroster = [mp1, mp2, mp3, mp4, mp5, mp6, mp7, mp8, mp9, mp10, mp11, mp12, mp13]
mypystarters = []
for player in mypyroster:
    if player.lineupSlot != 'BE' or player.lineupSlot != 'IR':
        mypystarters.append(player)

for player in mypystarters:
    player_avg_dict = player.stats['2023']['avg']
    
    for key in player_avg_dict.keys():
        if key == 'PTS':
            value = int(player_avg_dict[key])
            myteam_avg_pts += value
        elif key == 'BLK':
            value = int(player_avg_dict[key])
            myteam_avg_blk += value
        elif key == 'STL':
            value = int(player_avg_dict[key])
            myteam_avg_blk += value
        elif key == 'AST':
            value = int(player_avg_dict[key])
            myteam_avg_ast += value
        elif key == 'REB':
            value = int(player_avg_dict[key])
            myteam_avg_ast += value
        elif key == 'FG%':
            value = int(player_avg_dict[key])
            myteam_avg_fgp += value
        elif key == 'FT%':
            value = int(player_avg_dict[key])
            myteam_avg_ftp += value
        elif key == '3PTM':
            value = int(player_avg_dict[key])
            myteam_avg_3pm += value
print(myroster[0].stats)

from nba_api.stats.endpoints import commonplayerinfo, commonteamroster
from nba_api.stats.static import players, teams
import time
import pandas as pd

df = pd.DataFrame(columns=["realname","team"])

year = '1946'
for team in teams.get_teams():
    print(team)
    for i in range(1945,2018):
        team_roster = commonteamroster.CommonTeamRoster(season=str(i)+'-'+str(i+1)[2:],team_id=team['id'])
        print(team_roster.common_team_roster.get_dict()['data'])
        for player in team_roster.common_team_roster.get_dict()['data']:
            df = df.append({'realname':player[3], 'team':team['abbreviation']}, ignore_index=True)
            print({'realname':player[3], 'team':team['abbreviation']})
        time.sleep(2)
df.drop_duplicates(inplace=True)
df.to_csv('players.csv')

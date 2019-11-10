import requests
import json

URL = "https://stats.nba.com/stats/leaguedashteamstats/"

PARAMS = {
    'Conference':'',
    'DateFrom':'',
    'DateTo':'',
    'Division':'',
    'GameScope':'',
    'GameSegment':'',
    'LastNGames':0,
    'LeagueID':'00',
    'Location':'',
    'MeasureType':'Base',
    'Month':1,
    'OpponentTeamID':0,
    'Outcome':'',
    'PORound':0,
    'PaceAdjust':'N',
    'PerMode':'PerGame',
    'Period':0,
    'PlayerExperience':'',
    'PlayerPosition':'',
    'PlusMinus':'N',
    'Rank':'N',
    'Season':'2017-18',
    'SeasonSegment':'',
    'SeasonType':'Regular Season',
    'ShotClockRange':'',
    'StarterBench':'',
    'TeamID':0,
    'TwoWay':0,
    'VsConference':'',
    'VsDivision':''
}

#need to trick API into thinking we're a browser
HEADERS = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'X-NewRelic-ID': 'VQECWF5UChAHUlNTBwgBVw==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin ',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2017-18&SeasonType=Regular%20Season&Month=1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'
}

montly_stats = {
    '10': {},
    '11': {},
    '12': {},
    '1': {},
    '2': {},
    '3': {},
    '4': {}
}

month_count = 1 #pretty ugly, do it better
for month in montly_stats:
    PARAMS['Month'] = month_count
    r = requests.get(url = URL, params = PARAMS, headers = HEADERS) 
    data = r.json()
    for team_info in data['resultSets'][0]['rowSet']:
        team_stats = {}
        team_stats['id'] = team_info[0]
        team_stats['name'] = team_info[1]
        team_stats['GP'] = team_info[2]
        team_stats['pts_avg'] = team_info[26]
        team_stats['fgm_avg'] = team_info[7]
        team_stats['fga_avg'] = team_info[8]
        team_stats['fga_prct'] = team_info[9]
        team_stats['3gm_avg'] = team_info[10]
        team_stats['3ga_avg'] = team_info[11]
        team_stats['3ga_prct'] = team_info[12]
        team_stats['ftm_avg'] = team_info[13]
        team_stats['fta_avg'] = team_info[14]
        team_stats['fta_prct'] =team_info[15]
        team_stats['oreb'] = team_info[16]
        team_stats['dreb'] = team_info[17]
        team_stats['reb'] = team_info[18]
        team_stats['ast'] = team_info[19]
        team_stats['tov'] = team_info[20]
        team_stats['stl'] = team_info[21]
        team_stats['blk'] = team_info[22]

        montly_stats[str(month)][team_info[1]] = team_stats
    month_count+=1

with open('team_stats_per_month.json', 'w') as fp:
    json.dump(montly_stats, fp)

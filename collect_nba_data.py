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
    'MeasureType':'Defense',
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

ratings = {
    'october': {},
    'november': {},
    'december': {},
    'january': {},
    'february': {},
    'march': {},
    'april': {}
}

month_count = 1 #pretty ugly, do it better
for month_rating in ratings:
    PARAMS['Month'] = month_count
    r = requests.get(url = URL, params = PARAMS, headers = HEADERS) 
    data = r.json()
    for team_info in data['resultSets'][0]['rowSet']:
        ratings[month_rating][team_info[1]] = team_info[7]
    month_count+=1

#print(ratings)

'''
{
    'october': {'Atlanta Hawks': 106.7, 'Boston Celtics': 98.1, 'Brooklyn Nets': 111.0, 'Charlotte Hornets': 101.7, 'Chicago Bulls': 106.7, 'Cleveland Cavaliers': 111.6, 'Dallas Mavericks': 110.5, 'Denver Nuggets': 105.6, 'Detroit Pistons': 104.3, 'Golden State Warriors': 110.9, 'Houston Rockets': 105.1, 'Indiana Pacers': 107.4, 'LA Clippers': 101.0, 'Los Angeles Lakers': 101.4, 'Memphis Grizzlies': 99.3, 'Miami Heat': 108.8, 'Milwaukee Bucks': 106.1, 'Minnesota Timberwolves': 114.6, 'New Orleans Pelicans': 105.6, 'New York Knicks': 104.9, 'Oklahoma City Thunder': 98.4, 'Orlando Magic': 103.7, 'Philadelphia 76ers': 106.3, 'Phoenix Suns': 108.5, 'Portland Trail Blazers': 99.7, 'Sacramento Kings': 107.3, 'San Antonio Spurs': 102.7, 'Toronto Raptors': 96.7, 'Utah Jazz': 97.9, 'Washington Wizards': 101.1}, 
    'november': {'Atlanta Hawks': 111.7, 'Boston Celtics': 100.3, 'Brooklyn Nets': 107.0, 'Charlotte Hornets': 111.9, 'Chicago Bulls': 109.5, 'Cleveland Cavaliers': 107.8, 'Dallas Mavericks': 104.3, 'Denver Nuggets': 108.7, 'Detroit Pistons': 106.2, 'Golden State Warriors': 99.6, 'Houston Rockets': 102.6, 'Indiana Pacers': 108.7, 'LA Clippers': 111.4, 'Los Angeles Lakers': 104.8, 'Memphis Grizzlies': 109.6, 'Miami Heat': 103.5, 'Milwaukee Bucks': 107.6, 'Minnesota Timberwolves': 106.1, 'New Orleans Pelicans': 107.4, 'New York Knicks': 107.6, 'Oklahoma City Thunder': 103.5, 'Orlando Magic': 112.0, 'Philadelphia 76ers': 103.8, 'Phoenix Suns': 110.4, 'Portland Trail Blazers': 101.0, 'Sacramento Kings': 110.9, 'San Antonio Spurs': 103.4, 'Toronto Raptors': 108.5, 'Utah Jazz': 105.0, 'Washington Wizards': 106.4}, 
    'december': {'Atlanta Hawks': 110.4, 'Boston Celtics': 105.4, 'Brooklyn Nets': 107.0, 'Charlotte Hornets': 105.9, 'Chicago Bulls': 106.5, 'Cleveland Cavaliers': 110.0, 'Dallas Mavericks': 108.0, 'Denver Nuggets': 107.8, 'Detroit Pistons': 104.4, 'Golden State Warriors': 103.8, 'Houston Rockets': 111.5, 'Indiana Pacers': 110.7, 'LA Clippers': 106.3, 'Los Angeles Lakers': 112.2, 'Memphis Grizzlies': 111.8, 'Miami Heat': 108.8, 'Milwaukee Bucks': 112.1, 'Minnesota Timberwolves': 109.9, 'New Orleans Pelicans': 112.3, 'New York Knicks': 106.0, 'Oklahoma City Thunder': 106.2, 'Orlando Magic': 111.0, 'Philadelphia 76ers': 106.6, 'Phoenix Suns': 110.0, 'Portland Trail Blazers': 108.5, 'Sacramento Kings': 112.7, 'San Antonio Spurs': 103.9, 'Toronto Raptors': 103.2, 'Utah Jazz': 109.6, 'Washington Wizards': 106.2}, 
    'january': {'Atlanta Hawks': 110.8, 'Boston Celtics': 99.1, 'Brooklyn Nets': 107.7, 'Charlotte Hornets': 106.5, 'Chicago Bulls': 112.9, 'Cleveland Cavaliers': 112.9, 'Dallas Mavericks': 108.3, 'Denver Nuggets': 108.7, 'Detroit Pistons': 110.3, 'Golden State Warriors': 112.6, 'Houston Rockets': 107.4, 'Indiana Pacers': 105.4, 'LA Clippers': 107.8, 'Los Angeles Lakers': 107.7, 'Memphis Grizzlies': 107.0, 'Miami Heat': 102.2, 'Milwaukee Bucks': 108.3, 'Minnesota Timberwolves': 109.4, 'New Orleans Pelicans': 107.3, 'New York Knicks': 110.9, 'Oklahoma City Thunder': 107.9, 'Orlando Magic': 112.6, 'Philadelphia 76ers': 104.0, 'Phoenix Suns': 112.1, 'Portland Trail Blazers': 110.7, 'Sacramento Kings': 111.0, 'San Antonio Spurs': 100.5, 'Toronto Raptors': 105.4, 'Utah Jazz': 105.9, 'Washington Wizards': 110.2}, 
    'february': {'Atlanta Hawks': 107.3, 'Boston Celtics': 109.4, 'Brooklyn Nets': 113.6, 'Charlotte Hornets': 113.6, 'Chicago Bulls': 111.8, 'Cleveland Cavaliers': 112.9, 'Dallas Mavericks': 112.1, 'Denver Nuggets': 116.9, 'Detroit Pistons': 108.4, 'Golden State Warriors': 106.3, 'Houston Rockets': 103.5, 'Indiana Pacers': 106.7, 'LA Clippers': 108.7, 'Los Angeles Lakers': 106.8, 'Memphis Grizzlies': 110.9, 'Miami Heat': 107.6, 'Milwaukee Bucks': 106.9, 'Minnesota Timberwolves': 112.6, 'New Orleans Pelicans': 107.1, 'New York Knicks': 111.7, 'Oklahoma City Thunder': 111.6, 'Orlando Magic': 112.3, 'Philadelphia 76ers': 102.2, 'Phoenix Suns': 116.3, 'Portland Trail Blazers': 107.9, 'Sacramento Kings': 114.5, 'San Antonio Spurs': 111.1, 'Toronto Raptors': 103.7, 'Utah Jazz': 101.4, 'Washington Wizards': 109.2}, 
    'march': {'Atlanta Hawks': 113.1, 'Boston Celtics': 103.7, 'Brooklyn Nets': 114.3, 'Charlotte Hornets': 112.3, 'Chicago Bulls': 112.7, 'Cleveland Cavaliers': 112.2, 'Dallas Mavericks': 107.7, 'Denver Nuggets': 113.1, 'Detroit Pistons': 105.0, 'Golden State Warriors': 107.1, 'Houston Rockets': 103.7, 'Indiana Pacers': 103.4, 'LA Clippers': 110.7, 'Los Angeles Lakers': 108.3, 'Memphis Grizzlies': 113.6, 'Miami Heat': 106.7, 'Milwaukee Bucks': 112.0, 'Minnesota Timberwolves': 113.0, 'New Orleans Pelicans': 106.3, 'New York Knicks': 114.6, 'Oklahoma City Thunder': 107.9, 'Orlando Magic': 104.9, 'Philadelphia 76ers': 102.3, 'Phoenix Suns': 113.9, 'Portland Trail Blazers': 104.7, 'Sacramento Kings': 109.1, 'San Antonio Spurs': 102.9, 'Toronto Raptors': 110.3, 'Utah Jazz': 97.5, 'Washington Wizards': 109.2}, 
    'april': {'Atlanta Hawks': 105.9, 'Boston Celtics': 106.4, 'Brooklyn Nets': 108.0, 'Charlotte Hornets': 108.6, 'Chicago Bulls': 112.3, 'Cleveland Cavaliers': 110.4, 'Dallas Mavericks': 111.3, 'Denver Nuggets': 107.5, 'Detroit Pistons': 109.0, 'Golden State Warriors': 113.0, 'Houston Rockets': 104.9, 'Indiana Pacers': 109.7, 'LA Clippers': 120.5, 'Los Angeles Lakers': 106.4, 'Memphis Grizzlies': 118.5, 'Miami Heat': 105.4, 'Milwaukee Bucks': 108.8, 'Minnesota Timberwolves': 107.5, 'New Orleans Pelicans': 100.5, 'New York Knicks': 109.5, 'Oklahoma City Thunder': 104.7, 'Orlando Magic': 104.7, 'Philadelphia 76ers': 102.2, 'Phoenix Suns': 108.5, 'Portland Trail Blazers': 103.6, 'Sacramento Kings': 98.9, 'San Antonio Spurs': 109.0, 'Toronto Raptors': 100.2, 'Utah Jazz': 98.0, 'Washington Wizards': 109.9}
}
'''

URL = "https://stats.nba.com/stats/leaguedashplayerstats/"

PARAMS = {
    'College':'',
    'Conference':'',
    'Country':'',
    'DateFrom':'',
    'DateTo':'',
    'Division':'',
    'DraftPick':'',
    'DraftYear':'',
    'GameScope':'',
    'GameSegment':'',
    'Height':'',
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
    'VsDivision':'',
    'Weight':''
}

#need to trick API into thinking we're a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

player_stats = {
    'october': {},
    'november': {},
    'december': {},
    'january': {},
    'february': {},
    'march': {},
    'april': {}
}

month_count = 1 #pretty ugly, do it better
for month_rating in ratings:
    PARAMS['Month'] = month_count
    r = requests.get(url = URL, params = PARAMS, headers = HEADERS) 
    #print(r.content)
    data = r.json()
    for player_info in data['resultSets'][0]['rowSet']:
        personal_stats = {}
        personal_stats['id'] = player_info[0]
        personal_stats['name'] = player_info[1]
        personal_stats['GP'] = player_info[5]
        personal_stats['min_avg'] = player_info[9]
        personal_stats['pts_avg'] = player_info[29]
        personal_stats['fgm_avg'] = player_info[10]
        personal_stats['fga_avg'] = player_info[11]
        personal_stats['fga_prct'] = player_info[12]
        personal_stats['3gm_avg'] = player_info[13]
        personal_stats['3ga_avg'] = player_info[14]
        personal_stats['3ga_prct'] = player_info[15]
        personal_stats['ftm_avg'] = player_info[16]
        personal_stats['fta_avg'] = player_info[17]
        personal_stats['fta_prct'] =player_info[18]
        personal_stats['oreb'] = player_info[19]
        personal_stats['dreb'] = player_info[20]
        personal_stats['reb'] = player_info[21]
        personal_stats['ast'] = player_info[22]
        personal_stats['tov'] = player_info[23]
        personal_stats['stl'] = player_info[24]
        personal_stats['blk'] = player_info[25]
        player_stats[month_rating][player_info[1]] = personal_stats
    month_count+=1

with open('player_stats_per_month.json', 'w') as fp:
    json.dump(player_stats, fp)
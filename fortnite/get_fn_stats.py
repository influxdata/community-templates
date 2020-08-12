#!/usr/bin/python

import os
import sys
import time
import json
import csv
import requests

if "FORTNITE_API_TOKEN" in os.environ:
    FORTNITE_API_TOKEN = os.environ.get('FORTNITE_API_TOKEN')
else:
    print('FORTNITE_API_TOKEN does not exist')
    sys.exit(1)

url = 'https://fortniteapi.io/stats'
season = 13

data_api = {}

def parse_data(data):
    data_api['name'] = data['name']
    data_api['season'] = data['season']
    data_api['account_level'] = data['account']['level']
    data_api['account_progress_pct'] = data['account']['progress_pct']

    data_api['solo_placetop1'] = data['global_stats']['solo']['placetop1']
    data_api['solo_placetop3'] = data['global_stats']['solo']['placetop3']
    data_api['solo_placetop5'] = data['global_stats']['solo']['placetop5']
    data_api['solo_placetop10'] = data['global_stats']['solo']['placetop10']
    data_api['solo_placetop25'] = data['global_stats']['solo']['placetop25']
    data_api['solo_kd'] = data['global_stats']['solo']['kd']
    data_api['solo_winrate'] = data['global_stats']['solo']['winrate']
    data_api['solo_kills'] = data['global_stats']['solo']['kills']
    data_api['solo_matchesplayed'] = data['global_stats']['solo']['matchesplayed']
    data_api['solo_minutesplayed'] = data['global_stats']['solo']['minutesplayed']
    data_api['solo_score'] = data['global_stats']['solo']['score']
    data_api['solo_playersoutlived'] = data['global_stats']['solo']['playersoutlived']

    data_api['duo_placetop1'] = data['global_stats']['duo']['placetop1']
    data_api['duo_placetop3'] = data['global_stats']['duo']['placetop3']
    data_api['duo_placetop5'] = data['global_stats']['duo']['placetop5']
    data_api['duo_placetop10'] = data['global_stats']['duo']['placetop10']
    data_api['duo_placetop25'] = data['global_stats']['duo']['placetop25']
    data_api['duo_kd'] = data['global_stats']['duo']['kd']
    data_api['duo_winrate'] = data['global_stats']['duo']['winrate']
    data_api['duo_kills'] = data['global_stats']['duo']['kills']
    data_api['duo_matchesplayed'] = data['global_stats']['duo']['matchesplayed']
    data_api['duo_minutesplayed'] = data['global_stats']['duo']['minutesplayed']
    data_api['duo_score'] = data['global_stats']['duo']['score']
    data_api['duo_playersoutlived'] = data['global_stats']['duo']['playersoutlived']

    data_api['squad_placetop1'] = data['global_stats']['squad']['placetop1']
    data_api['squad_placetop3'] = data['global_stats']['squad']['placetop3']
    data_api['squad_placetop5'] = data['global_stats']['squad']['placetop5']
    data_api['squad_placetop10'] = data['global_stats']['squad']['placetop10']
    data_api['squad_placetop25'] = data['global_stats']['squad']['placetop25']
    data_api['squad_kd'] = data['global_stats']['squad']['kd']
    data_api['squad_winrate'] = data['global_stats']['squad']['winrate']
    data_api['squad_kills'] = data['global_stats']['squad']['kills']
    data_api['squad_matchesplayed'] = data['global_stats']['squad']['matchesplayed']
    data_api['squad_minutesplayed'] = data['global_stats']['squad']['minutesplayed']
    data_api['squad_score'] = data['global_stats']['squad']['score']
    data_api['squad_playersoutlived'] = data['global_stats']['squad']['playersoutlived']
    
    return data_api

data_api_list = []

with open('/etc/telegraf/players.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        acct_id = row['acct_id']
        pro = row['pro']
        player_name = row['player_name']

        response = requests.get(url,
                        headers = {'Authorization': FORTNITE_API_TOKEN},
                        params={'account': acct_id,
                                'season': season
                                }
                    )

        data = response.json()

        # if account level is set to 'None', "Show on Career Leaderboard" may be set to Off
        if data['account']['level']:
            data_api_dict = parse_data(data)
            data_api_dict['acct_id'] = acct_id
            data_api_dict['pro'] = pro
            data_api_list.append(data_api_dict.copy())

            time.sleep(5)

api_output = json.dumps(data_api_list)

if not data_api_list:
    print('No players found.')
else:
    print(api_output)

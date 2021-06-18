import requests
import numpy
import pandas
import json

def getPlayersByCountry(country):
    URL = "https://api.chess.com/pub/country/" + country + "/players"
    countryPlayers = requests.get(URL)
    data = countryPlayers.content
    with open(country + '_players.json', 'wb') as f:
        f.write(data)

def getPlayerStats(username):
    URL = "https://api.chess.com/pub/player/" + username + "/stats"
    playerStats = requests.get(URL)
    data = playerStats.content
    with open(username+'_stats.json', 'wb') as f:
        f.write(data)



f = open('AU_players.json','r')
player_list_json = json.load(f)

dictionary = {}

for user in ['jwrf']: #player_list_json['players']:
    print(user)
    URL = "https://api.chess.com/pub/player/" + user + "/stats"
    playerStats = requests.get(URL)
    data = playerStats.json()

    try:
        dictionary[user] = {
            'Rapid Rating': data['chess_rapid']['last']['rating'],
            'Puzzle Rating':data['tactics']['highest']['rating']
        }
    except:
        pass
    print(dictionary)







#for i in player_list_json['players']:
    #print(i)


f.close()




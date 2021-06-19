import requests
import numpy as np
import pandas as pd
import json
import matplotlib as mpl





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


def getPlayerData(country, n):
    URL = "https://api.chess.com/pub/country/" + country + "/players"
    countryPlayers = requests.get(URL)
    player_list_json = countryPlayers.json()
    dictionary = {}
    c = 0
    for user in player_list_json['players']:  # player_list_json['players']:
        if c >= n:
            break
        print(c)
        URL = "https://api.chess.com/pub/player/" + user + "/stats"
        playerStats = requests.get(URL)
        data = playerStats.json()

        try:
            dictionary[user] = {
                'Username': user,
                'Rapid Rating': data['chess_rapid']['last']['rating'],
                'Blitz Rating': data['chess_blitz']['last']['rating'],
                'Puzzle Rating': data['tactics']['highest']['rating']
            }
            c = c + 1
        except:
            pass
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    return df


def main():
    df = getPlayerData('AU', 10000)
    df.to_csv('AU_stats.csv', index = False)

if __name__ == '__main__':
    main()
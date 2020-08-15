import requests
#from lol_analyze import api_key

api_key = "RGAPI-4940ccfa-e08d-4beb-b779-337d8663674b"
# API requests
def requestSummonerName(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

def requestSummonerMastery(region, summonerID):
    URL = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/" + summonerID+ "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

def requestMatchList(region, accountID):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID+ "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

def requestMatchInfo(region, matchID):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v4/matches/" + matchID + "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

'''
For next time:
Because this is a comparison tool, maybe focus on that.
    After plot, SummonerA on avg gets 2.0cspm more than SummonerB.
Now is the time to include roles played.
    Input: Which role do you want to analyze(Offer 5)
    Only search thru that role and output
I prob don't need to repeat the same search and have 2 variable names for summoner1 & 2? Figure out a way with short list?
'''


import requests
import matplotlib.pyplot as plt
import numpy as np

# https://developer.riotgames.com/   for api key
api_key = "RGAPI-ba183118-506e-4779-aa19-cb411b59c933"

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

# Plotting comparisons of players' data
def plot_bar_kda():
    index = np.arange(len(kda))
    width = 0.3    
    index2 = np.arange(len(kda2))
    rect1 = plt.bar(index, kda, width, color='b')
    rect2 = plt.bar(index2 + width, kda2, width, color='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('KDA score', fontsize=10)
    plt.title('Avg KillDeathAssist Ratio over ' + str(matchCounter) + ' games')
    plt.legend( (rect1[0], rect2[0]), (summonerName + ' (' + str(avg_kda) + ')'\
                                       , summonerName2 + ' (' + str(avg_kda2) + ')') )
    plt.show()

def plot_bar_dpm():
    index = np.arange(len(dpm))
    width = 0.3    
    index2 = np.arange(len(dpm2))
    rect1 = plt.bar(index, dpm, width, color='b')
    rect2 = plt.bar(index2 + width, dpm2, width, color='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('DPM score', fontsize=10)
    plt.title('Avg DamagePerMin over ' + str(matchCounter) + ' games')
    plt.legend( (rect1[0], rect2[0]), (summonerName + ' (' + str(avg_dpm) + ')'\
                                       , summonerName2 + ' (' + str(avg_dpm2) + ')') )
    plt.show()

def plot_bar_cspm():
    index = np.arange(len(cspm))
    width = 0.3    
    index2 = np.arange(len(cspm2))
    rect1 = plt.bar(index, cspm, width, color='b')
    rect2 = plt.bar(index2 + width, cspm2, width, color='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('CSPM score', fontsize=10)
    plt.title('Avg CreepScorePerMin over ' + str(matchCounter) + ' games')
    plt.legend( (rect1[0], rect2[0]), (summonerName + ' (' + str(avg_cspm) + ')'\
                                       , summonerName2 + ' (' + str(avg_cspm2) + ')') )
    plt.show()
    
def plot_bar_gpm():
    index = np.arange(len(gpm))
    width = 0.3    
    index2 = np.arange(len(gpm2))
    rect1 = plt.bar(index, gpm, width, color='b')
    rect2 = plt.bar(index2 + width, gpm2, width, color='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('GPM score', fontsize=10)
    plt.title('Avg GoldPerMin over ' + str(matchCounter) + ' games')
    plt.legend( (rect1[0], rect2[0]), (summonerName + ' (' + str(avg_gpm) + ')'\
                                       , summonerName2 + ' (' + str(avg_gpm2) + ')') )
    plt.show()
    
def plot_bar_vision():
    index = np.arange(len(vision))
    width = 0.3    
    index2 = np.arange(len(vision2))
    rect1 = plt.bar(index, vision, width, color='b')
    rect2 = plt.bar(index2 + width, vision2, width, color='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('Vision score', fontsize=10)
    plt.title('Avg Vision score over ' + str(matchCounter) + ' games')
    plt.legend( (rect1[0], rect2[0]), (summonerName + ' (' + str(avg_vision) + ')'\
                                       , summonerName2 + ' (' + str(avg_vision2) + ')') )
    plt.show()
    

# Get region and user info as input
region = (str)(input("Type in a region: "))
summonerName = (str)(input("Type in your summoner name: "))
summonerName2 = (str)(input("Type in a second summoner name: "))

# Find information about user from in-game(public) name
name_JSON = requestSummonerName(region, summonerName)
name_JSON2 = requestSummonerName(region, summonerName2)

# Set variables to the corresponding data in JSON file
summonerID = name_JSON['id']
accountID = name_JSON['accountId']
summonerMastery = requestSummonerMastery(region, summonerID)
summonerID2 = name_JSON2['id']
accountID2 = name_JSON2['accountId']
summonerMastery2 = requestSummonerMastery(region, summonerID2)

# Find list of player's matches to extract data from
matchlist_JSON = requestMatchList(region, accountID)

# Set empty lists
matchId = []
kda = []
dpm = []
vision = []
gpm = []
cspm = []
matchCounter = 0

# View player's 100 most recent games
for matchNo in range(100):
    # We only want relevant Summoner's Rift Games. queue: 400, 420
    if matchlist_JSON['matches'][matchNo]['queue'] == 400 \
    or matchlist_JSON['matches'][matchNo]['queue'] == 420:
        matchId.append(matchlist_JSON['matches'][matchCounter]['gameId'])
        matchID = str(matchId[matchCounter])
        match_JSON = requestMatchInfo(region, matchID)
        matchCounter += 1
        
        # Find correct participant(player) in a single match
        if len(match_JSON) > 5:
            for pNo in range(10):
                participantName = match_JSON['participantIdentities'][pNo]['player']['summonerName']
                participantName = str(participantName)
                if (participantName.lower() == summonerName.lower()):
                    partID = match_JSON['participantIdentities'][pNo]['participantId']
                    break

        # Find in-game statistics from JSON file and put into variables
        for pNo in range(10):
            if (match_JSON['participants'][pNo]['participantId'] == partID):
                gameDuration = match_JSON['gameDuration']
                kills = match_JSON['participants'][pNo]['stats']['kills']
                assists = match_JSON['participants'][pNo]['stats']['assists']
                deaths = match_JSON['participants'][pNo]['stats']['deaths']        
                if(deaths == 0):
                    deaths = 1
                totalDamageDealtToChampions = match_JSON['participants'][pNo]['stats']['totalDamageDealtToChampions']
                visionScore = match_JSON['participants'][pNo]['stats']['visionScore']
                goldEarned = match_JSON['participants'][pNo]['stats']['goldEarned']
                totalMinionsKilled = match_JSON['participants'][pNo]['stats']['totalMinionsKilled']
                neutralMinionsKilled = match_JSON['participants'][pNo]['stats']['neutralMinionsKilled']

        # Append variable data into corresponding lists
        kda.append(round((kills + assists) / deaths, 2))
        dpm.append(round(totalDamageDealtToChampions/gameDuration*60, 2))
        vision.append(visionScore)
        gpm.append(round(goldEarned/gameDuration*60, 2))
        cs = totalMinionsKilled + neutralMinionsKilled
        cspm.append(round(cs/gameDuration*60, 2))
        if matchCounter == 30: # 30 most recent relevant matches
            break

avg_kda = round(sum(kda)/matchCounter, 2)
avg_dpm = round(sum(dpm)/matchCounter, 2)
avg_cspm = round(sum(cspm)/matchCounter, 2)
avg_gpm = round(sum(gpm)/matchCounter, 2)
avg_vision = int(sum(vision)/matchCounter)


# Repeat same search as above for Summoner2
matchlist_JSON2 = requestMatchList(region, accountID2)
matchId2 = []
kda2 = []
dpm2 = []
vision2 = []
gpm2 = []
cspm2 = []
matchCounter2 = 0
for matchNo in range(100):
    if matchlist_JSON2['matches'][matchNo]['queue'] == 400 \
    or matchlist_JSON2['matches'][matchNo]['queue'] == 420:
        matchId2.append(matchlist_JSON2['matches'][matchCounter2]['gameId'])
        matchID2 = str(matchId2[matchCounter2])
        match_JSON2 = requestMatchInfo(region, matchID2)
        matchCounter2 += 1
    
        if len(match_JSON2) > 5:
            for pNo in range(10):
                participantName2 = match_JSON2['participantIdentities'][pNo]['player']['summonerName']
                participantName2 = str(participantName2)
                if (participantName2.lower() == summonerName2.lower()):
                    partID2 = match_JSON2['participantIdentities'][pNo]['participantId']
                    break

        for pNo in range(10):
            if (match_JSON2['participants'][pNo]['participantId'] == partID2):
                gameDuration = match_JSON2['gameDuration']
                kills = match_JSON2['participants'][pNo]['stats']['kills']
                assists = match_JSON2['participants'][pNo]['stats']['assists']
                deaths = match_JSON2['participants'][pNo]['stats']['deaths']        
                if(deaths == 0):
                    deaths = 1
                totalDamageDealtToChampions = match_JSON2['participants'][pNo]['stats']['totalDamageDealtToChampions']
                visionScore = match_JSON2['participants'][pNo]['stats']['visionScore']
                goldEarned = match_JSON2['participants'][pNo]['stats']['goldEarned']
                totalMinionsKilled = match_JSON2['participants'][pNo]['stats']['totalMinionsKilled']
                neutralMinionsKilled = match_JSON2['participants'][pNo]['stats']['neutralMinionsKilled']
        
        kda2.append(round((kills + assists) / deaths, 2))
        dpm2.append(round(totalDamageDealtToChampions/gameDuration*60, 2))
        vision2.append(visionScore)
        gpm2.append(round(goldEarned/gameDuration*60, 2))
        cs = totalMinionsKilled + neutralMinionsKilled
        cspm2.append(round(cs/gameDuration*60, 2))
        if matchCounter2 == 30:# or matchCounter2 == matchCounter:
            break

avg_kda2 = round(sum(kda2)/matchCounter, 2)
avg_dpm2 = round(sum(dpm2)/matchCounter, 2)
avg_cspm2 = round(sum(cspm2)/matchCounter, 2)
avg_gpm2 = round(sum(gpm2)/matchCounter, 2)
avg_vision2 = int(sum(vision2)/matchCounter)


plot_bar_kda()
plot_bar_dpm()
plot_bar_cspm()
plot_bar_gpm()
plot_bar_vision()

#print("avg kda: ", round(avg_kda, 2))
#print("Total Account Mastery:", summonerMastery)


# Compare cspm
if avg_cspm > avg_cspm2:
    print("\nOn average, "+summonerName+" gets an average of "+str(avg_cspm)+" cs/min more than "+summonerName2+".")
else:
    print("\nOn average, "+summonerName2+" gets an average of "+str(avg_cspm)+" cs/min more than "+summonerName+".")

print(summonerName+"'s total Champion Mastery: "+str(summonerMastery))
print(summonerName2+"'s total Champion Mastery: "+str(summonerMastery2))



import matplotlib.pyplot as plt
import numpy as np

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


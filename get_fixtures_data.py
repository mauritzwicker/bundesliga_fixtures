####################################################################################################
#IMPORTS
from webdriver_creater import Webdriver


import time
from bs4 import BeautifulSoup
import bs4
import pandas as pd
from datetime import datetime
from datetime import timedelta
####################################################################################################

############## Functions
#to get the score of the fixture
def get_score_fixture(bs_bundesliga):
    #we get the results element which is the current-result
    current_result_bselement = bs_bundesliga.soup.findAll("div", attrs={'class': 'current-result'})
    current_result_bselement = current_result_bselement[0]  #to get it from ResultSet to element.Tag

    #get the score information
    score_home = current_result_bselement.findAll("span", attrs={'class': 'scoreboard'})
    # this is a <class 'bs4.element.ResultSet'>

    #if the result is None -> Before game -> continue

    if (len(score_home) == 0):
        # print('Before Game Start')
        return(0,0)
        #before the game
    else:
        #if during/after it is ex: [<span class="scoreboard">1</span>, <span class="scoreboard">1</span>]
        # -> get the score:
        #get the score
        goals_game_home = score_home[0].contents
        goals_game_home = int(goals_game_home[0])
        goals_game_away = score_home[1].contents
        goals_game_away = int(goals_game_away[0])
        # print('Score: {0} - {1}'.format(goals_game_home, goals_game_away))
        return(goals_game_home,goals_game_away)
#to get the status (time and what)
def get_status_fixture(bs_bundesliga):
    info_status_bselement = bs_bundesliga.soup.findAll("div", attrs={'class': 'info-status mstat'})
    info_status_bselement = info_status_bselement[0]    #to get it from ResultSet to element.Tag

    #get the timing information
    info_game_status = info_status_bselement.text
    if (len(info_game_status) == 0):
        game_stat_notplayed = 'Before Game Start'
        # print(game_stat_notplayed)
        return(game_stat_notplayed)
        #before the game
    else:
        # print(info_game_status)
        return(info_game_status)

    #If game finished (will give Finished)
    #if game hasn't started no data
    #If game ongoing:
    # 2nd Half - 60 
#to get the logos
def get_logos_fixture(bs_bundesliga):
    # to get the logos of teams in the fixture

    img_url_base = 'https://www.scoreboard.com'

    logs_game = bs_bundesliga.soup.findAll("img")
    home_image = img_url_base + str(logs_game[0]['src'])
    home_team = str(logs_game[0]['alt'])
    away_image = img_url_base + str(logs_game[1]['src'])
    away_team = str(logs_game[1]['alt'])
    #home_team and away_team is the name
    #home_image and away_image is the logo url
    # print(home_team)
    # print(home_image)
    # print(away_team)
    # print(away_image)
    return(home_team, away_team, home_image, away_image)


if __name__ == "__main__":
    #to run the codes

    #####################################################################################
    ############# PART 2 Go to the Fixtures Individual pages #################
    #####################################################################################

    #now we want to take the data of the games and go to their individual pages

    #we will do it with the example:
    # 6  g_1_GnujamRG  Werder Bremen         Hoffenheim  25.10  18:00
    # url : https://www.scoreboard.com/en/match/GnujamRG/#match-summary
    #so after we have to make it so it loops through for the game
    # https://www.scoreboard.com/en/match/A9vfb7tN/#match-summary

    id_val = 'g_1_GnujamRG'
    id_val = 'g_1_A9vfb7tN'
    # id_val = 'g_1_MDVzL6Oe'
    id_url = id_val[4:]
    url_fixture = 'https://www.scoreboard.com/en/match/' + str(id_url) + '/#match-summary'

    #we create our beautifulsoupObject which is type: <class '__main__.Webdriver'>
    bs_bundesliga = Webdriver(url_fixture)

    #list to hold info on the current fixture/game
    curr_fixture_info = []
    # this is now goals home, goals away, game status, home team, away team, home url, away url

    #get the score
    goals_home, goals_away = get_score_fixture(bs_bundesliga)
    curr_fixture_info.append(goals_home)
    curr_fixture_info.append(goals_away)
    #get game stats
    game_stat = get_status_fixture(bs_bundesliga)
    curr_fixture_info.append(game_stat)
    #get team names and logo urls
    home_team, away_team, home_image, away_image = get_logos_fixture(bs_bundesliga)
    curr_fixture_info.append(home_team)
    curr_fixture_info.append(away_team)
    curr_fixture_info.append(home_image)
    curr_fixture_info.append(away_image)

    #to display the games info on terminal
    if True:
        print()
        print('{0} - {1}'.format(curr_fixture_info[3], curr_fixture_info[4]))
        print('{0} : {1}'.format(curr_fixture_info[0], curr_fixture_info[1]))
        print('{0}'.format(curr_fixture_info[2]))
        print()













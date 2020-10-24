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
#to get the game info for all fixtures (first scrape)
def get_info_fixturespage(matches):
    fixtures = pd.DataFrame([], columns = ['id', 'home', 'away', 'date', 'time'])

    #loop through each game and add the info to the dataframe
    for fixture in matches:
        #list to hold the data for this one fixture
        # fitxture_info = []

        #get all the information for each game
        game_id = fixture.get('id')
        game_home = fixture.find('div', attrs={'class': 'event__participant event__participant--home'}).contents
        game_home = game_home[0]
        game_away = fixture.find('div', attrs={'class': 'event__participant event__participant--away'}).contents
        game_away = game_away[0]
        game_datetime = fixture.find('div', attrs={'class': 'event__time'}).contents
        game_datetime = str(game_datetime[0])
        game_date = game_datetime[:5]
        game_time = game_datetime[-5:]

        #add all the information for each game to a list
        information_game = [str(game_id), str(game_home), str(game_away), str(game_date), str(game_time)]
        #create that list into a pandas object
        a_series = pd.Series(information_game, index = fixtures.columns)
        #append the object to the dataframe
        fixtures = fixtures.append(a_series, ignore_index=True)
    #return the dataframe with all the games with info on the fixtures page
    return(fixtures)

#to get the dataframe of todays fixtures
def get_todays_fixtures_info(fixtures):
    #fixtures is the df with all the fixtures on the fixtures page
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    date_today = str(currentDay) + '.' + str(currentMonth)

    #only get the fixtures that are being played today
    fixtures_today = fixtures[fixtures['date'] == date_today]

    #we return the fixtures pd with info on todays fixtures
    return(fixtures_today)
#to get the dataframe of tomorrows fixtures
def get_tomorrows_fixtures_info(fixtures):
    #fixtures is the df with all the fixtures on the fixtures page
    tomorrowDay = (datetime.now() + timedelta(days=1)).day
    tomorroMonth = (datetime.now() + timedelta(days=1)).month
    date_tomorrow = str(tomorrowDay) + '.' + str(tomorroMonth)

    #only get the fixtures that are being played today
    fixtures_tomorrow= fixtures[fixtures['date'] == date_tomorrow]

    #we return the fixtures pd with info on tomorrows fixtures
    return(fixtures_tomorrow)
#to get the dataframe of overtomorrows fixtures
def get_overtomorrows_fixtures_info(fixtures):
    #fixtures is the df with all the fixtures on the fixtures page
    overtomorrowDay = (datetime.now() + timedelta(days=2)).day
    overtomorroMonth = (datetime.now() + timedelta(days=2)).month
    date_overtomorrow = str(overtomorrowDay) + '.' + str(overtomorroMonth)

    #only get the fixtures that are being played today
    fixtures_overtomorrow= fixtures[fixtures['date'] == date_overtomorrow]

    #we return the fixtures pd with info on overtomorrows fixtures
    return(fixtures_overtomorrow)
#display games on terminal
def display_games_terminal(todays_bundesliga_fixtures_df, tomorrow_bundesliga_fixtures_df, overtomorrow_bundesliga_fixtures_df):
    print()
    print('    Todays Fixtures    ')
    print(todays_bundesliga_fixtures_df)
    print()
    print('    Tomorrows Fixtures    ')
    print(tomorrow_bundesliga_fixtures_df)
    print()
    print('    Overtomorrows Fixtures    ')
    print(overtomorrow_bundesliga_fixtures_df)
    print()
#to save todays fixtures
def save_todays_fixture(todays_fixtures):
    try:
        todays_fixtures.to_csv(r'./today_fixtures.csv', index = False, header = False)
        return(True)
    except:
        return(False)






if __name__ == "__main__":
    #to run the codes

    #####################################################################################
    ############# PART 1 Get the Games from Bundesliga-Fixtures-Page #################
    #####################################################################################

    ### CREATE BEAUTIFULSOUP OBJECT ###
    #to create a new bs4 parse (main_url of countries playing)
    url_bundesliga = "https://www.scoreboard.com/en/soccer/germany/bundesliga/fixtures/"
    #we create our beautifulsoupObject which is type: <class '__main__.Webdriver'>
    bs_bundesliga = Webdriver(url_bundesliga)

    ### FIND EACH MATCH LISTED ON FIXTURES PAGE ###
    #we create our list of elements with that title and is of type: <class 'bs4.element.ResultSet'>
    results_matchtoday = bs_bundesliga.soup.findAll("div", title='Click for match detail!')
    #each element in results_matchtoday is of type: <class 'bs4.element.Tag'>

        #MAYBE ADD THE OPTION TO HAVE THE SCORE ALREADY ON THAT PAGE (so that if we only want the score)

    ### CREATE PANDAS DATAFRAME WITH ALL FIXTURES INFO ###
    #we now send the results_matchtoday to the get_info_fixturespage and append all the data to a DF
    bundesliga_fixtures_df = get_info_fixturespage(results_matchtoday)
    #we get back a pandas dataframe that holds all the fixtures info on the fixtures page

    ### FILTER DATAFRAME FOR TODAYS FIXTURES ###
    #we go to the get_todays_fixtures_info function to filter the games down to the ones today
    todays_bundesliga_fixtures_df = get_todays_fixtures_info(bundesliga_fixtures_df)
    tomorrow_bundesliga_fixtures_df = get_tomorrows_fixtures_info(bundesliga_fixtures_df)
    overtomorrow_bundesliga_fixtures_df = get_overtomorrows_fixtures_info(bundesliga_fixtures_df)

    #To dsplay the games on terminal
    display_games = False
    if display_games:
        display_games_terminal(todays_bundesliga_fixtures_df, tomorrow_bundesliga_fixtures_df, overtomorrow_bundesliga_fixtures_df)

    #save to file
    saved = save_todays_fixture(todays_bundesliga_fixtures_df)
    if saved:
        print('saved Todays fixtures')
    else:
        print('unable to save Todays fixtures')


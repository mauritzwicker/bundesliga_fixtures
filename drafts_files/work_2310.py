# https://www.scoreboard.com/en/soccer/germany/bundesliga/fixtures/

####################################################################################################
#IMPORTS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import bs4
import requests
from urllib.request import urlopen as uReq
import pandas as pd
from datetime import datetime
from datetime import timedelta
####################################################################################################

####################################################################################################
#NOTES
'''
- have to load this script in the morning because when the games are running it no longer finds them
- IDEA HAVE THIS RUN ON THE PI ALL THE TIME AND BE IN STANDBY WHEN NO GAME

So Far:
- Part 1:
    we can get the list of all fixtures (with info) in bundesliga page and cut it down to who is playing today, tomorrow, overtomorrow
- Part 2:
    we can get the score, status, and logos from the fixtures page for a pixture given the id
- Part 3:
- Part 4:

To Do:
- Part 1:
    we need to save this list as a file so that we can access it
- Part 2:
    we need to format the info so that we have it in a useful way
- Part 3:
    we want to get the lineup data or other interesting data about the fixture (look at options)
    maybe move this to part 4 bcs all extra
- Part 4:
    how to move the data around between different parts of the script
    implement it in a script that calls this repeatedly so that we get informative data
    show that data onto terminal/rgb matrix
- Part 5:
    make the code nice and readable (multiple files, objects ...)


'''
####################################################################################################




####################################################################################################
#Code

class Webdriver:
    #FUNCTIONS TO EXTRACT URL WITH CHROMEDRIVER AND BS4

    def __init__(self, arg1):
        self.url = arg1
        self.driver = self.create_webdriver()
        self.content = self.get_webdriver_content()
        self.soup = self.extract_bs4_from_web()
        self.quit_driver()


    def quit_driver(self):
        driver = self.driver    #do we need this?
        #### To quit the driver
        driver.quit()
        return()
    def extract_bs4_from_web(self):
        content = self.content  #do we need this?
        #### Parse the webdriver using html
        soup = BeautifulSoup(content,"html.parser")
        return(soup)
    def get_webdriver_content(self):
        driver = self.driver    #do we need this?
        #### Encode the webdriver page
        content = driver.page_source.encode('utf-8').strip()
        return(content)
    def create_webdriver(self):
        #### Create the webdriver given the url
        url = self.url      #do we need this?
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(url)
        #to close the drive as soon as loaded (find a way to not open it at all)
        time.sleep(0)
        return(driver)


############## Part 1 Functions
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


############## Part 2 Functions
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
    if True:
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


    # WE WILL SAVE THIS AS A FILE SO THAT WE CAN ACCESS IT














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


















####################################################################################################

#main.py

############################
#to control the live_html information codes
#main class to pass information on what information we need

# class __init__():
    #go to main controlling code to find the specific information





### look at lsw code for outline


#other py files to make:
#dictionary of which teams to look for


#### WHAT ELSE TO LOOK FOR
#time, lineup, ... team names, ...
#make it so that it finds all the games that are relevant, go to that games individual page and from there finds the info
####################




















'''



## CODE ADJUSTMENTS 24.06

####################################################################################################
#IMPORTS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import bs4
####################################################################################################




####################################################################################################
#DEFINE INITIAL URL TO SCRAPE
url = 'https://www.scoreboard.com/en/soccer/'
####################################################################################################





############################### functions of individual actions ###############################
####################################################################################################
#FUNCTIONS TO EXTRACT URL WITH CHROMEDRIVER AND BS4
def quit_driver(driver):
    #### To quit the driver
    driver.quit()
    return()
def extract_bs4_from_web(content):
    #### Parse the webdriver using html
    soup = BeautifulSoup(content,"html.parser")
    return(soup)
def get_webdriver_content(driver):
    #### Encode the webdriver page
    content = driver.page_source.encode('utf-8').strip()
    return(content)
def create_webdriver(url):
    #### Create the webdriver given the url
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url)
    #to close the drive as soon as loaded (find a way to not open it at all)
    time.sleep(0)
    return(driver)
####################################################################################################
####################################################################################################
#FUNCTIONS TO SCRAPE BS4-ELEMENT AND GET CURRENT COUNTRIES PLAYING
def find_curr_countries(soup):
    ####To get the bs4 items of current countries where games are being played
    countries_playing_bs = soup.findAll("span",{"class":"event__title--type"})
    return(countries_playing_bs)
def create_list_countries_playing():
    ####Initialize list for countries that are currently playing
    current_countries = []
    return(current_countries)
def scrape_countries_list(countries_playing_bs, current_countries):
    ####Take all different country items in the bs4 item and append them to the list
    for ctry_ind, ctry in enumerate(countries_playing_bs):
        #all the countries are listed in a common format that they are listed between [33:-7] in the str
        country_item = str(ctry)[33:-7]
        current_countries.append(country_item)
    return(current_countries)
####################################################################################################
####################################################################################################
#FUNCTIONS TO GO INTO THE COUNTRIES WEBPAGE AND PARSE THEM
def country_url(country, url):
    ####To get the url for each country that is playing
    #change the country name to lowercase
    ctr = str(country).lower()
    #define the new url
    url_country = url + ctr + '/'
    return(url_country)
def country_driver(url):
    driver_country = create_webdriver(url_country)
    #get the content from the driver (so get the developer elements stuff)
    content_country = get_webdriver_content(driver_country)
    #parse content into html using BeautifulSoup
    soup_country = extract_bs4_from_web(content_country)
    #quit the driver
    quit_driver(driver_country)
    return(soup_country)
####################################################################################################




############################### functions guiding process of steps ###############################
####################################################################################################
#FUNCTION TO GUIDE THE CREATION OF A DRIVER AND GETTING THE BS4 ELEMENT FROM A URL
def guide_parse(url):
    #create the webdriver
    driver = create_webdriver(url)
    #get the content from the driver (so get the developer elements stuff)
    content = get_webdriver_content(driver)
    #parse content into html using BeautifulSoup
    soup = extract_bs4_from_web(content)
    #quit the driver
    quit_driver(driver)
    return(soup)
####################################################################################################

####################################################################################################
#FUNCTION TO GUIDE THE SCRAPING OF THE BS4-ELEMENT FOR COUNTRIES THAT ARE PLAYING
def guide_scrape_countries(soup):
    #get the country items from bs4-element
    countries_playing_bs = find_curr_countries(soup)
    #initialize list of countries that are playing
    current_countries = create_list_countries_playing()
    #get the actual country names from countries_playing_bs and append to current_countries
    current_countries = scrape_countries_list(countries_playing_bs, current_countries)
    return(current_countries)
####################################################################################################

####################################################################################################
#FUNCTION TO GUIDE THE CREATION OF A DRIVER FOR COUNTRIES
def guide_parse_countries(countries):
    for country in countries:
        #get the country url
        url_country = country_url(country, url)

        #create the country webdriver
        soup_country = country_driver(url_country)

        #now we need to scrape for the leagues in the country (but cant go back bcs in for loop!)




####################################################################################################









####################################################################################################
#def __init__():

################################################################################
#FIRST PARSE FOR MAIN URL (returns bs4_html_parse)
soup_main = guide_parse(url)
################################################################################

################################################################################
#FIRST SCRAPE FOR MAIN URL (returns what countries are playing)
current_countries = guide_scrape_countries(soup_main)
print(current_countries)
################################################################################

################################################################################
#SECOND PARSE FOR COUNTRIES' URL (returns bs4_html_parse)
soup_main = guide_parse_countries(url)
################################################################################

####################################################################################################





    #now to find the current games (in the leagues of the countries)

    #leagues in current country
    country_leagues = soup_country.findAll("span",{"class":"event__title--name"})
    print(country_leagues)

    #finitialize array to hold all the leagues, in the country, that are currently playing
    country_leagues_playing = []
    #go through the leagues in the country and add the league name
    for x in country_leagues:
        print(x['title'])
        country_leagues_playing.append(x['title'])

    #now find the hrefs for the leagues playing
    link_country_leagues = soup_country.findAll("ul",{"class":"menu selected-country-list"})
    print(link_country_leagues)
    link_country_leagues = link_country_leagues[0]

    #initalize list to hold all the links (we need to do this bcs some li items have more than 1 link (1 Bundi, 2 Bundi,...))
    lst_tags_all = []

    for li_ind, li in enumerate(link_country_leagues):
        #to filter out the items in league_small_list_bs that are not of the datatype that we want
        if type(li) is not bs4.element.Tag:
            continue
        #to get all the href-links for the leagues
        tags = li.find_all('a', href=True)
        #go through all the tags (href-links) in the li item
        for tag in tags:
            #append each href link to lst_tags_all list
            if str(tag['href'])[0:11] != '/en/soccer/':
                continue
            elif len(str(tag['href'])) <= 2:
                continue
            else:
                lst_tags_all.append(tag['href'])
    # print(lst_tags_all)

    for ind_league, league in enumerate(lst_tags_all):
        #
        soup_league = country_to_curr_league(league, country_leagues_playing[ind_league])

        quit() #dont want to do it for all in practice

    return(soup_country)


















quit()








'''




















### MAKE OBJECT ORIENTED

####################################################################################################
#IMPORTS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import bs4
####################################################################################################


#we need three main classes:
# 1. country (for a country that is playing)
# 2. league (for a league that is playing in that country)
# 3. game (for a game that is playing in that league)
# 4. more for things inside the game

class Country: #Define a country that is playing today

    def __init__(self, arg1, arg2):
        self.name = 'country' #change to the country name
        self.url = arg2 + str(arg1).lower() + '/' #change to the country url
        self.status = 'playing today' #for if they are playing or not (always yes...)

class League: #Define a league that is playing today in the country

    def __init__(self, arg1, arg2, arg3, arg4):
        #arg1 = country
        #arg2 = league_href (so the league url)
        #arg3 = url
        #arg4 = url_base
        self.country_name = arg1  #country name
        self.url = str(arg4) + str(arg2) #league_url
        self.status = 'playing today' #for if they are playing or not (always yes...)
        front = len(url)
        front = int(front + len(self.country_name) + 1)
        self.url_fixtures = self.url + 'fixtures/'  #change to the leagues' fixtures url
        self.league_name = self.url[front:-1]

class Game: #Define a game that is playing today in the league in the country

    def __init__(self, arg1, arg2, arg3, arg4, arg5):

        #arg1 = country
        #arg2 = league_href (so the league url)
        #arg3 = url
        #arg4 = url_base
        #arg5 = game

        self.country_name = arg1 #country name
        self.url_league = str(arg4) + str(arg2) #league url
        self.status = 'playing today' #for if they are playing or not (always yes...)
        front = len(url)
        front = int(front + len(self.country_name) + 1)
        self.url_fixtures = self.url_league + 'fixtures/'  #change to the leagues' fixtures url
        self.league_name = self.url_league[front:-1] #league name

        self.home_team = arg5[0] #home team name
        self.away_team = arg5[1] #away team name
        self.game_id = arg5[2] #the game id
        self.game_calendar = arg5[3] #the time/date of the game (format ex. = '11.07. 12:30')
        self.date = self.game_calendar[:5] #the date of the game
        self.time = self.game_calendar[7:12] #the time of the game

        self.url_game_summary = str(arg4) + '/en/match/' + str(self.game_id[4:]) + '/#match-summary'
        self.url_game_statistics = str(arg4) + '/en/match/' + str(self.game_id[4:]) + '/#match-statistics;0'
        self.url_game_lineups = str(arg4) + '/en/match/' + str(self.game_id[4:]) + '/#lineups;1'



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

class Scrape_countries: #class to scrape the overview bs4 element for the countries playing
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE BS4-ELEMENT FOR COUNTRIES THAT ARE PLAYIN

    def __init__(self, arg1):
        self.overview_obj = arg1
        #get the country items from bs4-element
        self.countries_playing_bs = self.find_curr_countries()
        #initialize list of countries that are playing
        self.create_list_countries_playing()
        #get the actual country names from countries_playing_bs and append to current_countries
        self.scrape_countries_list()

    def find_curr_countries(self):
        overview = self.overview_obj #necessery?
        soup = overview.soup
        ####To get the bs4 items of current countries where games are being played
        countries_playing_bs = soup.findAll("span",{"class":"event__title--type"})
        return(countries_playing_bs)
    def create_list_countries_playing(self):
        ####Initialize list for countries that are currently playing
        self.current_countries = []
    def scrape_countries_list(self):
        ####Take all different country items in the bs4 item and append them to the list
        for ctry_ind, ctry in enumerate(self.countries_playing_bs):
            #all the countries are listed in a common format that they are listed between [33:-7] in the str
            country_item = str(ctry)[33:-7]
            # print(country_item)
            self.current_countries.append(country_item)

class Scrape_league: #class to scrape the countries bs4 element for the leagues playing
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE BS4-ELEMENT FOR LEAGUES THAT ARE PLAYIN

    def __init__(self, arg1):
        self.overview_obj = arg1
        #get the league items from bs4-element
        self.leagues_playing_bs = self.find_curr_leagues()
        #get the href items from bs4-element
        self.leagues_playing_href = self.find_href_curr_leagues()
        # print(len(self.leagues_playing_href))
        # print(len(self.leagues_playing_bs))

        #for now we will leave out the creating of dict bcs we dont really need the league name atm

        # #initialize dict of leagues that are playing and href
        # self.create_dict_leagues_playing()
        # #get the actual league names from leagues_playing_bs and append to current_leagues
        # self.scrape_leagues_list()

    def find_curr_leagues(self):
        overview = self.overview_obj #necessery?
        soup = overview.soup
        ####To get the bs4 items of current leagues where games are being played
        leagues_playing_bs = soup.findAll("span",{"class":"event__title--name"})
        #finitialize array to hold all the leagues, in the country, that are currently playing
        country_leagues_playing = []
        #go through the leagues in the country and add the league name
        # print(leagues_playing_bs)
        for x in leagues_playing_bs:
            # print(x['title'])
            country_leagues_playing.append(x['title'])
        return(country_leagues_playing)
    def find_href_curr_leagues(self):
        #now find the hrefs for the leagues playing
        overview = self.overview_obj #necessery?
        soup = overview.soup
        link_country_leagues = soup.findAll("ul",{"class":"menu selected-country-list"})
        # print(link_country_leagues)
        link_country_leagues = link_country_leagues[0]
        #initalize list to hold all the links (we need to do this bcs some li items have more than 1 link (1 Bundi, 2 Bundi,...))
        lst_tags_all = []

        for li_ind, li in enumerate(link_country_leagues):
            #to filter out the items in league_small_list_bs that are not of the datatype that we want
            if type(li) is not bs4.element.Tag:
                continue
            #to get all the href-links for the leagues
            tags = li.find_all('a', href=True)
            #go through all the tags (href-links) in the li item
            for tag in tags:
                #append each href link to lst_tags_all list
                if str(tag['href'])[0:11] != '/en/soccer/':
                    continue
                elif len(str(tag['href'])) <= 2:
                    continue
                else:
                    lst_tags_all.append(tag['href'])
        return(lst_tags_all)
        # print(lst_tags_all)
    def create_dict_leagues_playing(self):
        ####Initialize dict for countries that are currently playing and their href
        self.current_leagues = {}
    def scrape_leagues_list(self):
        ####Take all different league items in the bs4 item and append them to the list and find the href
        for i in range(0, len(self.leagues_playing_bs)):
            # print(self.leagues_playing_bs[i])
            # print(self.leagues_playing_href[i])
            # print()
            self.current_leagues[self.leagues_playing_bs[i]] = self.leagues_playing_href[i]
        # print(self.current_leagues)
        quit()  #only bcs we dont want it to run forever when we just try it out

class Scrape_game: #class to scrape the leagues bs4 element for the games being played
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE BS4-ELEMENT FOR GAMES THAT ARE BEING PLAYED

    def __init__(self, arg1):
        self.overview_obj = arg1
        #get the game items from bs4-element
        self.lst_teams_home = self.get_curr_games_home()
        # print(self.lst_teams_home)
        self.lst_teams_away = self.get_curr_games_away()
        # print(self.lst_teams_home)
        self.lst_game_ids = self.get_curr_games_id()
        # print(self.lst_game_ids)
        self.lst_game_times = self.get_curr_games_time()
        # print(self.lst_game_times)
        self.fixtures = self.names_curr_games()
        # print(self.fixtures)

    def get_curr_games_home(self):
        games_playing_home_bs = []
        # for link in self.overview_obj.soup.findAll("div", {"class": "event__participant event__participant--home"}, {"class": "event__participant event__participant--home fontBold"}):
        A = "event__participant event__participant--home"
        B = "event__participant event__participant--home fontBold"
        for link in self.overview_obj.soup.findAll("div", {"class": re.compile(r"A|B")}):
            games_playing_home_bs.append(str(link.get_text()))
            print(str(link.get_text()))
        return(games_playing_home_bs)

    def get_curr_games_away(self):
        games_playing_away_bs = []
        for link in self.overview_obj.soup.findAll("div", {"class": "event__participant event__participant--away"}):
            games_playing_away_bs.append(str(link.get_text()))
        return(games_playing_away_bs)

    def get_curr_games_id(self):
        ids_games = []
        for link in self.overview_obj.soup.findAll("div", {"title": "Click for match detail!"}):
            ids_games.append(str(link.get('id')))
        return(ids_games)

    def get_curr_games_time(self):
        times_games = []
        for link in self.overview_obj.soup.findAll("div", {"class": "event__time"}):
            times_games.append(str(link.get_text()))
        return(times_games)

    def names_curr_games(self):
        if len(self.lst_teams_home) != len(self.lst_teams_away) != len(self.lst_game_ids) != len(self.lst_game_times):
            print('SOMETHING WRONG')
            quit()
        else:
            fixtures = []
            for i in range(0, len(self.lst_teams_home)):
                game_info = [self.lst_teams_home[i], self.lst_teams_away[i], self.lst_game_ids[i], self.lst_game_times[i]]
                fixtures.append(game_info)
        return(fixtures)

class Match_information: #class to scrape the match for all data we want
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE MATCH STATISTICS

    def __init__(self, arg1, arg2):
        self.overview_obj = arg1
        self.game_obj = arg2
        self.game_score = self.get_score()

    def get_score(self):
        score_game = ''
        for link in self.overview_obj.soup.findAll("div", {"class": "current-result"}):
            score_game = str(link.get_text())
        print(score_game)
        return(score_game)


class Match_information_match_summary:    #class to scrape the individual matches for the match summary overview page
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE GAMES

    def __init__(self, arg1, arg2):
        self.overview_obj = arg1
        self.game_obj = arg2

        #for before game
        print(self.get_players_missing())

        #for during game


    def get_part_image(self):
        #function to get the images/logo of the participating teams
        print()
        return()

    def get_players_missing(self):
        #function to get the players that are missing the game/injured
        players = []

        table = self.overview_obj.soup.find("table", {"id": "missing-players"})

        rows=list()
        for row in table.findAll("tr"):
           rows.append(row)
           print(row)
           print(str(row.get_text()))

        return()

class Match_information_match_statistics:   #class to scrape the individual matches for the match statistics page
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE GAMES
    #ONLY WHEN GAME IS IN PLAY

    def __init__(self, arg1, arg2):
        self.overview_obj = arg1
        self.game_obj = arg2

        #for before game

        #for during game

class Match_information_lineups:     #class to scrape the individual matches for the match lineup page
    #FUNCTIONS TO GUIDE THE SCRAPING OF THE GAMES
    #ONLY WHEN GAME IS IN PLAY

    def __init__(self, arg1, arg2):
        self.overview_obj = arg1
        self.game_obj = arg2

        #for before game

        #for during game







if __name__ == "__main__":
    #to run the codes

    #to create a new bs4 parse (main_url of countries playing)
    url = 'https://www.scoreboard.com/en/soccer/'
    url_base = 'https://www.scoreboard.com'
    overview = Webdriver(url)   #so overview is the object of the webdriver that contains the url, soup, ...

    #to create new scrape of overview parse
    overview_data = Scrape_countries(overview)   #so overview_data is the object that contains the list of countries
    # print(type(overview_data))
    # print(overview_data)
    # print(overview_data.current_countries)
    # print(type(overview_data.current_countries))

    #so far it works and gives us the countries in  a list (all caps)
    #now for county in overview_data.current_countries create a country object and then same with leagues usw
    for country in overview_data.current_countries:
        print(country)
        country_page = Country(country, url)     #so we create the country object (which is the country webpage)
        country_ovw = Webdriver(country_page.url)   #so we create the webdriver object for the country
        country_data = Scrape_league(country_ovw)   #so we create the data (scrape) the country for leagues

        for league_href in country_data.leagues_playing_href:
            print(league_href)
            #league_href = the league href
            #country = the country name
            league_page = League(country, league_href, url, url_base) #so we create the league object (which is the league webpage)
            #league_page.name = league name
            #league_page.url = league url
            league_ovw = Webdriver(league_page.url)     #so we create the webdriver object for the league
            league_data = Scrape_game(league_ovw)     #so we create the data (scrape) for games

            for game in league_data.fixtures:
                print(game)
                #game = list(home team, away team, game id, time/date)
                game_page = Game(country, league_href, url, url_base, game)
                game_ovw = Webdriver(game_page.url_game_summary)     #so we create the webdriver object for match_summary
                game_data = Match_information(game_ovw, game_page)      #so we create the data (scrape) for the summary in the game

                #*********************
                #if time before kick off: (and include checks to see if it exists)


                '''
                #if we need to do it with individual tabs (but it think not)
                game_ovw_matchsumm = Webdriver(game_page.url_game_summary)     #so we create the webdriver object for match_summary
                game_data_summary = Match_information_match_summary(game_ovw_matchsumm, game_page)      #so we create the data (scrape) for the summary in the game


                game_ovw_matchstats = Webdriver(game_page.url_game_statistics)     #so we create the webdriver object for match_statistics
                game_data_stats = Match_information_match_statistics(game_ovw_matchstats, game_page)      #so we create the data (scrape) for the stats in the game

                game_ovw_lineups = Webdriver(game_page.url_game_lineups)     #so we create the webdriver object for match_lineups
                game_data_lineups = Match_information_lineups(game_ovw_lineups, game_page)      #so we create the data (scrape) for the lineup in the game


                '''


                ###check if we need all these or it its enough to just get the overall game page and find it like that




                quit()
        #so country_data.current_leagues is the dictionary with leagues and the
        #check if country_data.countr_ovw.url gives us the country url



        #now we have the league and we want it to return the list of leagues and href's for those leagues
        #now we create individual league objects (like for the countries) and do the same to find all games
        #then we create the game objects and bam!


    print()


#SO APPARENTLY FIXTURES PAGE ONLY SHOWS FUTURE GAMES (SO EITHER HAVE TO RUN THIS BEFORE GAMES START TO GET ID OR CHANGE CODE)






quit()







### add option to get the results straight from start page so that it doesnt take ages and go into each individual page






#need to make it get each indiv link for leagues bcs quali usw uses same link





























































































quit()


### first write code on how to get what information we need (then add into nice object oriented code outline)

#####################################################################################################################
####################################### IMPORTS #######################################
#####################################################################################################################
#to import the necessery libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import bs4

#####################################################################################################################
#####################################################################################################################


#####################################################################################################################
####################################### EXTRACT INFORMATION FROM ULR USING BS4 #######################################
#####################################################################################################################
#to scrape the url using BeautifulSoup and get all the data (not just source code)
print()
print('START: EXTRACT INFORMATION FROM ULR USING BS4')

#thi is for the Overview Page for Football (we want to then go into the individual leagues/countries/games)
url_overview = 'https://www.scoreboard.com/en/soccer/'

#create driver and stuff for the overview page
driver_overview = webdriver.Chrome(ChromeDriverManager().install())
driver_overview.maximize_window()
driver_overview.get(url_overview)
#to close the drive as soon as loaded (find a way to not open it at all)
time.sleep(0)
#get the content from the driver (so get the developer elements stuff)
content_overview = driver_overview.page_source.encode('utf-8').strip()
#parse it in html using BeautifulSoup
soup_overview = BeautifulSoup(content_overview,"html.parser")
driver_overview.quit()

print('END: EXTRACT INFORMATION FROM ULR USING BS4')
print()
#####################################################################################################################
#####################################################################################################################


#####################################################################################################################
####################################### GET CURRENT LEAGUES + COUNTRY INFO #######################################
#####################################################################################################################
#this is to get the names of countries and leagues that are playing atm
print()
print('START: GET CURRENT LEAGUES + COUNTRY INFO')

#to get the bs4 items of current countries where games are being played
location_event_bs = soup_overview.findAll("span",{"class":"event__title--type"})
#to get the bs4 items of current leagues where games are being played
league_event_bs = soup_overview.findAll("span",{"class":"event__title--name"})

#now make these into a league/list
#now we have to select the first element (which is all of it bcs bs4 does it like that)

#initialize dict for countries and leagues that are currently playing
current_countries_leagues = {}
#initialize list for countries and leagues that are currently playing
current_countries = []
current_leagues = []

#now we take all different country items in the bs4 item and append them to the list
for ctry_ind, ctry in enumerate(location_event_bs):
    #all the countries are listed in a common format that they are listed between [33:-7] in the str
    country_item = str(ctry)[33:-7]
    current_countries.append(country_item)

#now we take all different league items in the bs4 item and append them to the list
for leag_ind, leag in enumerate(league_event_bs):
    current_leagues.append(leag['title'])

#now we want to create a dictionary for the leagues and countries
for i in range(0, len(current_countries)):
    country = current_countries[i]
    league = current_leagues[i]
    #we have to use league as they key bcs some countries have more than one league
    current_countries_leagues.update({league : country} )

#print the league-country dictionary
# for x in current_countries_leagues:
#     print(x, current_countries_leagues[x])
print(current_countries_leagues)

print('END: GET CURRENT LEAGUES + COUNTRY INFO')
print()
#####################################################################################################################
#####################################################################################################################


#####################################################################################################################
####################################### GET THE DICT FOR THE BIG LEAGUES #######################################
#####################################################################################################################
### this is to get the dictionary of big leagues and the corresponiding href address/link
print()
print('START: GET THE DICT FOR THE BIG LEAGUES')

#list of big leagues ()
big_leages_links = {}   #dict with title of big leagues and their href link (without basis link)

#bs4.element.ResultSet that has all the big leagues
league_list_bs = soup_overview.findAll("ul",{"id":"my-leagues-list"})
#now we have to select the first element (which is all of it bcs bs4 does it like that)
league_list_bs = league_list_bs[0]
#define item_size to create if loop to leave out ResultSet items that are in league_list_bs but we dont want (bcs empty or...)
item_size = 0
#go through the ResultsSet to find each different <li title > item
for li_ind, li in enumerate(league_list_bs):
    #to find the length of the correct items that we want (taking first as reference and then saying they are the largest ones)
    if li_ind == 0:
        item_size = len(li)
    elif len(li) > item_size:
        item_size = len(li)
    #to check if the item is not smaller (ie filter out those we dont want)
    if len(li) != item_size:
        continue
    #to get the title of the li item (ex. title = "ENGLAND: PREMIER LEAGUE")
    title = li['title']
    #to get the href link of the li item (ex. href  = "/en/soccer/england/premier-league/")
    link = li.find('a', href=True)['href']
    #to append the title and href-link of each item to the dictionary holding them
    big_leages_links.update({title : link} )

    ####later maybe add to csv file or so to save everything externally and only go and get it once

#print the big league-address/link dictionary
# for x in big_leages_links:
#     print(x, big_leages_links[x])
print(big_leages_links)

print('END: GET THE DICT FOR THE BIG LEAGUES')
print()
#####################################################################################################################
#####################################################################################################################



#####################################################################################################################
####################################### GET THE DICT FOR ALL THE LEAGUES #######################################
#####################################################################################################################
### this is to get the dictionary of all the leagues and the corresponiding href address/link
print()
print('START: GET THE DICT FOR ALL THE LEAGUES')
#list of big leagues ()
small_leagues_links = {}   #dict with title of all(small) leagues and their href link (without basis link)

#bs4.element.ResultSet that has all the leagues
league_small_list_bs = soup_overview.findAll("ul",{"class":"menu country-list tournament-menu"})
#now we have to select the first element (which is all of it bcs bs4 does it like that)
league_small_list_bs = league_small_list_bs[0]
#define item_size to create if loop to leave out ResultSet items that are in league_list_bs but we dont want (bcs empty or...)
item_size = 0
#go through the ResultsSet to find each different <li title > item
for li_ind, li in enumerate(league_small_list_bs):
    #to filter out the items in league_small_list_bs that are not of the datatype that we want
    if type(li) is not bs4.element.Tag:
        continue
    #to filter out the items in league_small_list_bs that are not of the type we want (not li)
    if str(li)[:6] != '<li id':
        continue
    #to get all the href-links for the leagues
    tags = li.find_all('a', href=True)
    #initalize list to hold all the links (we need to do this bcs some li items have more than 1 link (1 Bundi, 2 Bundi,...))
    lst_tags_all = []
    #go through all the tags (href-links) in the li item
    for tag in tags:
        #append each href link to lst_tags_all list
        lst_tags_all.append(tag['href'])

    #create item that makes the whole li item (titles, link, usw) into a string so that we can get the name of the link
    txt_item = str(li)

    #we want to find the text between the >< pointers bcs that is where the text is (like when finding the score)
    c_start = '>'
    c_end = '<'
    #now we look for all the positions in the string that hold the > character
    arr_start_pos = [pos for pos, char in enumerate(txt_item) if char == c_start]
    #now we look for all the positions in the string that hold the < character
    arr_end_pos = [pos for pos, char in enumerate(txt_item) if char == c_end]
    #initilize the list that will hold all these string names that we find (to later cross-reference with hrefs)
    lst_titles_all = []

    #go thruogh all the > items found (minus 1 because it always starts with < and ends with >)
    for i in range(0, len(arr_start_pos) -1):
        #find the difference between all > and < (skipping the first < and last >)
        diff_ind = arr_end_pos[i+1] - arr_start_pos[i]
        #to filter out the ones where no text ist (bcs it also occurs when a subitem just ends)
        if diff_ind <=1:
            continue
            #so if it is "...><..." insteead of "...>text<..." we skip that one
        else:
            #we now get the text (the name) that is between the two >< we identified
            title = txt_item[arr_start_pos[i]+1:arr_end_pos[i+1]]
            #we append them to the list for all titles (to cross reference with href)
            lst_titles_all.append(title)

    #now we make the href list and titles list into (key, item) items for the dictionary holding all league links
    for j in range(0, len(lst_titles_all)):
        #the title is the name from between the >text<
        title = lst_titles_all[j]
        #the link is the href from findall
        link = lst_tags_all[j]
        #append them to the dictionary
        small_leagues_links.update({title : link} )

#print the dictionary
# for y in small_leagues_links:
#     print(y, small_leagues_links[y])
print(small_leagues_links)
print('END: GET THE DICT FOR ALL THE LEAGUES')
print()
#####################################################################################################################
#####################################################################################################################

#####################################################################################################################
####################################### GO INTO THE SPECIFIC LEAGUE WEBPAGE #######################################
#####################################################################################################################
#this is to go into the specific leagues page (from overview page) for current games
print()
print('START: GO INTO THE SPECIFIC LEAGUE WEBPAGE')

#to go into the current leagues from overview_to_curr_country
def country_to_curr_league(infom, league_name):
    #infom is the href for the league
    #league_name is the name of the league

    # url_overview defined in beginning as : 'https://www.scoreboard.com/en/soccer/'
    #go back by 11 bcs we dont want /en/soccer/
    url_league = url_overview[:-11] + infom

    driver_league = webdriver.Chrome(ChromeDriverManager().install())
    driver_league.maximize_window()
    driver_league.get(url_league)
    #to close the drive as soon as loaded (find a way to not open it at all)
    time.sleep(10)
    #get the content from the driver (so get the developer elements stuff)
    content_league = driver_league.page_source.encode('utf-8').strip()
    #parse it in html using BeautifulSoup
    soup_league= BeautifulSoup(content_league,"html.parser")

    # print(soup_country)
    print(type(soup_league))
    driver_league.quit()

    return(soup_league)

#to go into the current country (and get the leagues):
def overview_to_curr_country(infom):
    #take the country and league name and href and go into that countries info
    ctr = infom[0]
    href_ctr = infom[1]
    leag = infom[2]
    # url_overview defined in beginning as : 'https://www.scoreboard.com/en/soccer/'
    #go back by 11 bcs we dont want /en/soccer/
    url_country = url_overview[:-11] + href_ctr

    driver_country = webdriver.Chrome(ChromeDriverManager().install())
    driver_country.maximize_window()
    driver_country.get(url_country)
    #to close the drive as soon as loaded (find a way to not open it at all)
    time.sleep(0)
    #get the content from the driver (so get the developer elements stuff)
    content_country = driver_country.page_source.encode('utf-8').strip()
    #parse it in html using BeautifulSoup
    soup_country = BeautifulSoup(content_country,"html.parser")

    # print(soup_country)
    print(type(soup_country))
    driver_country.quit()

    #now to find the current games (in the leagues of the countries)

    #leagues in current country
    country_leagues = soup_country.findAll("span",{"class":"event__title--name"})
    print(country_leagues)

    #finitialize array to hold all the leagues, in the country, that are currently playing
    country_leagues_playing = []
    #go through the leagues in the country and add the league name
    for x in country_leagues:
        print(x['title'])
        country_leagues_playing.append(x['title'])

    #now find the hrefs for the leagues playing
    link_country_leagues = soup_country.findAll("ul",{"class":"menu selected-country-list"})
    print(link_country_leagues)
    link_country_leagues = link_country_leagues[0]

    #initalize list to hold all the links (we need to do this bcs some li items have more than 1 link (1 Bundi, 2 Bundi,...))
    lst_tags_all = []

    for li_ind, li in enumerate(link_country_leagues):
        #to filter out the items in league_small_list_bs that are not of the datatype that we want
        if type(li) is not bs4.element.Tag:
            continue
        #to get all the href-links for the leagues
        tags = li.find_all('a', href=True)
        #go through all the tags (href-links) in the li item
        for tag in tags:
            #append each href link to lst_tags_all list
            if str(tag['href'])[0:11] != '/en/soccer/':
                continue
            elif len(str(tag['href'])) <= 2:
                continue
            else:
                lst_tags_all.append(tag['href'])
    # print(lst_tags_all)

    for ind_league, league in enumerate(lst_tags_all):
        #
        soup_league = country_to_curr_league(league, country_leagues_playing[ind_league])

        quit() #dont want to do it for all in practice

    return(soup_country)

#initialize multidim list with all the lists of country, country link, and league
info_curr_games_lvl1 = []
for leag in current_countries_leagues:
    #initialize each individual list for all the data
    info_spec_league = []
    #now we get the country for that league (bcs first we want to go into the country)
    ctr = current_countries_leagues[leag]
    ctr = str(ctr).lower()
    ctr = ctr.title()
    spec_link = small_leagues_links[ctr]
    #now we want to append the country, the country link, and the league
    info_spec_league.append(ctr)
    info_spec_league.append(spec_link)
    info_spec_league.append(leag)
    info_curr_games_lvl1.append(info_spec_league)

for i in info_curr_games_lvl1:
    soup_country = overview_to_curr_country(i)

    #


    quit() #dont want to do it for all in practice




######
##ok to do:
# - write into nice functions and classes how to go from overview to country to league
# - then decide what functions we want (ie get the current scores, get past scores, )
# - add features to go into current games => info on players and stuff...






##***** need to find out how
def find_href_curr_leagues(self):
    #now find the hrefs for the leagues playing
    overview = self.overview_obj #necessery?
    soup = overview.soup
    link_country_leagues = soup.findAll("ul",{"class":"menu selected-country-list"})
    # print(link_country_leagues)
    link_country_leagues = link_country_leagues[0]
    #initalize list to hold all the links (we need to do this bcs some li items have more than 1 link (1 Bundi, 2 Bundi,...))
    lst_tags_all = []

    for li_ind, li in enumerate(link_country_leagues):
        #to filter out the items in league_small_list_bs that are not of the datatype that we want
        if type(li) is not bs4.element.Tag:
            continue
        #to get all the href-links for the leagues
        tags = li.find_all('a', href=True)
        #go through all the tags (href-links) in the li item
        for tag in tags:
            #append each href link to lst_tags_all list
            if str(tag['href'])[0:11] != '/en/soccer/':
                continue
            elif len(str(tag['href'])) <= 2:
                continue
            else:
                lst_tags_all.append(tag['href'])
    return(lst_tags_all)
    # print(lst_tags_all)
def create_dict_leagues_playing(self):
    ####Initialize dict for countries that are currently playing and their href
    self.current_leagues = {}
def scrape_leagues_list(self):
    ####Take all different league items in the bs4 item and append them to the list and find the href
    for i in range(0, len(self.leagues_playing_bs)):
        print(self.leagues_playing_bs[i])
        print(self.leagues_playing_href[i])
        print()
        self.current_leagues[leagues_playing_bs[i]] = leagues_playing_href[i]

    quit()
##*****


#so we have the dict current_countries_leagues of leagues:countries that currently have games
#and we have the dict small_leagues_links of leagues:link of all leagues

#initialize each individual lis

#we should have:
# - pair for league name: => link
# - current games being played (ie leauges with games)
# so take the current games being played, take league name, get the link, go into the link and from there find all
# the current games, find all the links to the games, and go into the current games

# for leg in current_countries_leagues:
#     #initialize each individual list for all the data
#     info_spec_league = []
#     ctr = current_countries_leagues[leg]
#     ctr = str(ctr).lower()
#     ctr = ctr.title()
#     print(ctr)
#     spec_link = small_leagues_links[ctr]
#     info_spec_league.append(ctr)
#     info_spec_league.append(spec_link)
#     print(spec_link)
# print(current_countries_leagues[leg])
# print(ctr)
# print(small_leagues_links[str(leg)])
# print(leg)




print()
#####################################################################################################################
#####################################################################################################################



def get_names_from_brac(self, lst_given):
    #we want to find the text between the >< pointers bcs that is where the text is (like when finding the score)
    c_start = '>'
    c_end = '<'
    #now we look for all the positions in the string that hold the > character
    arr_start_pos = [pos for pos, char in enumerate(lst_given) if char == c_start]
    print(arr_start_pos)
    #now we look for all the positions in the string that hold the < character
    arr_end_pos = [pos for pos, char in enumerate(lst_given) if char == c_startr]
    print(arr_end_pos)
    #initilize the list that will hold all these string names that we find (to later cross-reference with hrefs)
    lst_titles_final = []

    #go thruogh all the > items found (minus 1 because it always starts with < and ends with >)
    for i in range(0, len(arr_start_pos) -1):
        #find the difference between all > and < (skipping the first < and last >)
        diff_ind = arr_end_pos[i+1] - arr_start_pos[i]
        #to filter out the ones where no text ist (bcs it also occurs when a subitem just ends)
        if diff_ind <=1:
            print('CONTINUE')
            continue
            #so if it is "...><..." insteead of "...>text<..." we skip that one
        else:
            #we now get the text (the name) that is between the two >< we identified
            title = lst_given[arr_start_pos[i]+1:arr_end_pos[i+1]]
            print(title)
            #we append them to the list for all titles (to cross reference with href)
            lst_titles_final.append(title)
    return(lst_titles_final)



###to do next:
# - get the current games in list or dict or so
# - for the current games go into the corresponding country/league urls => into the game link
# - from there get the actual game data (so not only score but lineup and stuff)


# need to import errors, so that if empty list is returned, so that it retries or quits or so







quit()


#variables atm:
# lst_locations := list of all the locations on the webpage
# lst_leagues := list of all the leagues on the webpage (leagues of the locations)
# lst_loc_leg_combine := list of all the leagues and locations combined as string
# big_leages_links := dict of country_league conbo and the href link (for the big leagues)
# small_leagues_links := dict of country league combo and the href link (for all leagues)
######

##3 guck mal ob man den webdriver uberhaupt brauch








































# print(league_list_bs)
# print(type(league_list_bs))
# print(len(league_list_bs))
# quit()
# for x in league_list_bs.find_all('li'):
#     print(x.text)

# print(type(league_list_bs))
# for tag in league_list_bs:
#     print(tag)
#     print(tag.find('a', href=True)['href'])


'''

#to get it for small leagues
def small_leagues_link(soup_overview, addres_league):
    #so now we want to go and look for it in the other leagues

    #need to go through all infor_event_bs = soup_overview.findAll("ul",{"class":"menu country-list tournament-menu"})
    #and get the country name and thus the href
    infor_event_bs = soup_overview.findAll("ul",{"class":"menu country-list tournament-menu"})
    for tag in infor_event_bs.find_all('a', href=True):
        print(type(tag))
        print(tag)
        print('ol')
        quit()



    infor_event_bs = soup_overview.findAll("ul",{"class":"menu country-list tournament-menu"})
    infor_event_bs = infor_event_bs.findAll("li",{"title":addres_league})
    # print(infor_event_bs)
    # print(infor_event_bs)
    for tag in infor_event_bs.find_all('a', href=True):
        print(tag['href'])
    # for tag in infor_event_bs:
    #     # print(tag)
    #     print(tag.find_all('a', href=True)['href'])
    #     print()
    #     print()



for addres_league in lst_loc_leg_combine:
    infor_event_bs = soup_overview.findAll("li",{"title":addres_league})
    #here look for it in a different fct but for now like this
    #check if in main leagues or rest
    if len(infor_event_bs) == 0:
        #so now we want to go and look for it in the other leagues
        small_leagues_link(soup_overview, addres_league)
        continue
    # print(infor_event_bs)
    for tag in infor_event_bs:
        print(tag.find('a', href=True)['href'])
    # link_event_bs = infor_event_bs.find('a')['href']
    # print(link_event_bs)





'''



# for item in league_list_bs:
#     #find the href
#     aaa = item.find_all('a', href=True)
#     # print(item)
#     print(aaa)
#     print()
#     print()



#for small leagues
# league_low_list_bs = soup_overview.findAll("ul",{"class":"menu country-list tournament-menu"})
# for item in league_low_list_bs:
#     print(item)
#     print()

# print(lst_loc_leg_combine)

# for addres_league in lst_loc_leg_combine:
#     link_event_bs = soup_overview.findAll("li",{"title":addres_league})
#     print(link_event_bs)



'''
### create a dictinary that takes the league and country and finds the link for the league
lst_locations = []
lst_leagues = []
lst_urls = []
for item in location_event_bs:
    xx_loc = item.text
    lst_locations.append(xx_loc)
    continue

for item in league_event_bs:
    xx_leg = item.text
    lst_leagues.append(xx_leg)
    continue

for link in soup_overview.find_all('a', href=True):
    xx_lk = link['href']
    if xx_lk[0:11] != "/en/soccer/":
        continue
    else:
        lst_urls.append(xx_lk)
        continue

# print(lst_locations)
# print(lst_leagues)
# print(lst_urls)
# print(len(lst_locations), len(lst_leagues), len(lst_urls))



dct_country_link = {} #has country and league as keys (combined bcs of Bundesliga1 and 2 zb.)
for i in range(0,len(lst_locations)):
    country_select = lst_locations[i]
    league_select = lst_leagues[i]
    dct_key_comb = str(country_select) + str(league_select)
    print(dct_key_comb)
    for j in lst_urls:
        if country_select in lst_urls
    val_link = lst_urls
'''



# print(location_event)
# print(location_event_vl)
# print(league_event)
# print()
# print(type(location_event_vl))
# print(location_event_vl['title'])


#<span class="event__title--type">SPAIN</span>
#<span class="event__title--name" title="LaLiga">LaLiga</span>



driver_overview.quit()


quit()






























# url = 'https://www.livescore.com/soccer/spain/segunda-division/rayo-vallecano-vs-albacete/1-3094462/'

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get(url)
# time.sleep(0)
# content = driver.page_source.encode('utf-8').strip()
# soup = BeautifulSoup(content,"html.parser")

# # lists = soup.findAll("div",{"data-type":"score"})
# lists_HOME = str(soup.findAll("span",{"class":"hom"}))
# lists_AWAY = str(soup.findAll("span",{"class":"awy"}))
# score_HOME = lists_HOME[-9:-8]
# score_AWAY = lists_AWAY[-9:-8]

# print('Score is {0} : {1}'.format(score_HOME, score_AWAY))

# driver.quit()




# quit()











#********************************
#
#
# MAKE WEB SCRAPING WITH ML
# INPUT SPECIFIC TERM => (LOOKING at specific webpages or in general google find the best results)
# find best results using ML and stuff
# or put in a webpage and what you want from it => find best result using ML and stuff
#
# need to learn html and other codes used for webpages
# need to learn BeautifulSoup and how webscraping works
# need to design a neural network for analyzing the scrape
# look up speed difference between using C/C++ or python
#
#
#
#********************************




import get_fixtures_data
from webdriver_creater import Webdriver

import pandas as pd
from datetime import datetime
from datetime import timedelta
import threading
import time


class Game_fixture():

    def __init__(self, fixture):
        self.fixtures_info = fixture
        cols_fixture = self.fixtures_info.keys()
        self.id_val = self.fixtures_info.get('id')
        self.hometeam = self.fixtures_info.get('home')
        self.awayteam = self.fixtures_info.get('away')
        self.dategame = self.fixtures_info.get('date')
        self.timegame = self.fixtures_info.get('time')
        self.scrape_frequency = 30    #scrape every __ seconds
        self.save_fixture_path = './fixtures_files/fixture_' + str(self.id_val) + '.csv'

        # id_val = 'g_1_GnujamRG'
        # id_val = 'g_1_A9vfb7tN'
        # id_val = 'g_1_MDVzL6Oe'
        self.id_url = self.id_val[4:]
        self.url_fixture = 'https://www.scoreboard.com/en/match/' + str(self.id_url) + '/#match-summary'

    def start_thread(self):
        self.game_thread = threading.Thread(target = self.get_info_game)
        # game_thread.start()
        return(self.game_thread)

    def make_webdriver(self):
        #we create our beautifulsoupObject which is type: <class '__main__.Webdriver'>
        self.bs_fixture = Webdriver(self.url_fixture)

    def first_scrape_game(self):
        # maybe use a dictionary not a list
        #list to hold info on the current fixture/game
        self.curr_fixture_info = []
        # this is now goals home, goals away, game status, home team, away team, home url, away url

        # add the date
        todays_date = datetime.now().day
        todays_month = datetime.now().month
        date_today = str(todays_date) + '.' + str(todays_month)
        self.curr_fixture_info.append(date_today)

        #get the score
        goals_home, goals_away = get_fixtures_data.get_score_fixture(self.bs_fixture)
        self.curr_fixture_info.append(goals_home)
        self.curr_fixture_info.append(goals_away)
        #get game stats
        game_stat = get_fixtures_data.get_status_fixture(self.bs_fixture)
        self.curr_fixture_info.append(game_stat)
        #get team names and logo urls
        home_team, away_team, home_image, away_image = get_fixtures_data.get_logos_fixture(self.bs_fixture)
        self.curr_fixture_info.append(home_team)
        self.curr_fixture_info.append(away_team)
        self.curr_fixture_info.append(home_image)
        self.curr_fixture_info.append(away_image)

        #save to file
        self.save_info_game()

        #to display the games info on terminal
        if True:
            print()
            print('{0} - {1}'.format(self.curr_fixture_info[4], self.curr_fixture_info[5]))
            print('{0} : {1}'.format(self.curr_fixture_info[1], self.curr_fixture_info[2]))
            print('{0}'.format(self.curr_fixture_info[3]))
            print('{0}'.format(self.curr_fixture_info[0]))
            print()


    def scrape_game_playing(self):
        ### scrape consistantly
        scrape_counter = 0

        while scrape_counter < (250 * self.scrape_frequency):
            ## scrape
            #get the score
            goals_home, goals_away = get_fixtures_data.get_score_fixture(self.bs_fixture)
            #get game stats
            game_stat = get_fixtures_data.get_status_fixture(self.bs_fixture)
            scrape_counter+=1

            self.curr_fixture_info[1] = goals_home
            self.curr_fixture_info[2] = goals_away
            self.curr_fixture_info[3] = game_stat

            self.save_info_game()
            time.sleep(self.scrape_frequency)

    def save_info_game(self):
        # self.curr_fixture_info
        # the data is: date, goals_home, goals_away, game_stat, home_team, away_team, home_image, away_image
        # we want to save this to a file with todays date
        # try:
        # print(self.save_fixture_path)
        # print(pd_save_game)
        a_series = pd.Series(self.curr_fixture_info, index = ['date', 'goals_home', 'goals_away', 'status', 'home', 'away', 'home_img', 'away_img'])
        pd_save_game = pd.DataFrame(a_series)
        pd_save_game.to_csv(self.save_fixture_path, index = False, header = False)
        # except:
            # print('save Unsuccessful')

    def get_info_game(self):
        #make webdriver

        #we create our beautifulsoupObject which is type: <class '__main__.Webdriver'>
        self.make_webdriver()

        #get the game data once to start
        self.first_scrape_game()

        #now scrape continuously
        self.scrape_game_playing()

        #here we get the information about the game and make it into an object that returns our inofmration from:
        #get_fixture_data.py



#if running without main.py
if __name__ == '__main__':

    t__start = time.perf_counter()

    # url_game = 'https://www.scoreboard.com/en/match/GnujamRG/#match-summary'
    game_info = ['g_1_GnujamRG', 'hometeam', 'awayteam', 'today', 'now']
    game_info_dict = {'id': game_info[0], 'home' : game_info[1], 'away': game_info[2], 'date': game_info[3], 'time': game_info[4]}
    game_info_pd = pd.Series(game_info_dict)

    game = Game_fixture(game_info_pd)
    t_game = game.start_thread()

    t__done = time.perf_counter()
    t__runtime = t__done - t__start
    print('Time to run: {0}'.format(t__runtime))


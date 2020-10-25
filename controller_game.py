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


        # id_val = 'g_1_GnujamRG'
        # id_val = 'g_1_A9vfb7tN'
        # id_val = 'g_1_MDVzL6Oe'
        self.id_url = self.id_val[4:]
        self.url_fixture = 'https://www.scoreboard.com/en/match/' + str(self.id_url) + '/#match-summary'

        print(self.fixtures_info)

    def start_thread(self):
        self.game_thread = threading.Thread(target = self.get_info_game)
        # game_thread.start()
        return(self.game_thread)

    def make_webdriver(self):
        #we create our beautifulsoupObject which is type: <class '__main__.Webdriver'>
        self.bs_fixture = Webdriver(self.url_fixture)

    def get_info_game(self):
        #make webdriver

        #we create our beautifulsoupObject which is type: <class '__main__.Webdriver'>
        self.make_webdriver()

        #list to hold info on the current fixture/game
        self.curr_fixture_info = []
        # this is now goals home, goals away, game status, home team, away team, home url, away url

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

        #to display the games info on terminal
        if True:
            print()
            print('{0} - {1}'.format(self.curr_fixture_info[3], self.curr_fixture_info[4]))
            print('{0} : {1}'.format(self.curr_fixture_info[0], self.curr_fixture_info[1]))
            print('{0}'.format(self.curr_fixture_info[2]))
            print()



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


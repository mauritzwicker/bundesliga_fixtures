from save_todays_fixtures import Todays_Fixtures
from webdriver_creater import Webdriver

import pandas as pd
from datetime import datetime
from datetime import timedelta
import time

class Bundesliga_fixtures():


    def __init__(self, url_scrape):
        self.url = url_scrape
        self.bs_bundesliga = Webdriver(self.url)
        self.todays_fix_saved = False

        self.last_date_saved = None         #the last date where we saved fixtures
        self.saved_todays_fix = False       #if we have saved todays fixtures
        self.todays_fix_file = './today_fixtures.csv'       #what file we save todays games in

        #step 1 check if gotten todays fixtures
        self.saved_todays_fix = self.check_today_fixtures_get()

        #is True if saved returns False if not saved
        if self.saved_todays_fix == False:
            self.save_fixtures()
            self.saved_todays_fix = self.check_today_fixtures_get()
            if (self.saved_todays_fix == False):
                print('Error cant save newest fixtures properly')
                quit()
            else:
                print('Todays fixtures gotten and checked')
        else:
            print('Already saved Todays ({0}) Fixtures'.format(self.last_date_saved))



    def check_today_fixtures_get(self):
        #get the last saved games data
        self.last_saved_games, self.nonempty_fixtures = Todays_Fixtures.get_fixtures_saved(self)
        #if self.nonempty_fixtures = False -> no games saved in txt file
        if (self.nonempty_fixtures == False):
            print('currently saved fixtures list empty')
            self.saved_todays_fix = False
            return(self.saved_todays_fix)
        else:
            #so if we at least have some fixtures saved in the csv
            #check if we have gotten todays fixtures
            self.last_date_saved, self.saved_todays_fix = Todays_Fixtures.fixtures_saved(self)

            if self.saved_todays_fix == True:
                # print('Today has been saved')
                return(self.saved_todays_fix)
            else:
                # print('Today has not been saved. Last saved date: {0}'.format(last_date_saved))
                return(self.saved_todays_fix)

    def save_fixtures(self):
        ###
        saved_now = Todays_Fixtures.save_fixtures_today(self)
        if saved_now == 1:
            self.saved_todays_fix == True
            todays_date = datetime.now().day
            todays_month = datetime.now().month
            date_today = str(todays_date) + '.' + str(todays_month)
            self.last_date_saved = date_today
        else:
            print('No games today, come back tomorrow...')
            # print('failed save fixtures')






#if running without main.py
if __name__ == '__main__':

    t_start = time.perf_counter()

    url_bundesliga = "https://www.scoreboard.com/en/soccer/germany/bundesliga/fixtures/"
    fixtures_today = Bundesliga_fixtures(url_bundesliga)

    print()
    print(fixtures_today.last_saved_games)
    print()

    t_done = time.perf_counter()
    t_runtime = t_done - t_start
    print('Time to run: {0}'.format(t_runtime))

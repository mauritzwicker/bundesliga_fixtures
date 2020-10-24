# from get_todays_fixtures import get_info_fixturespage, get_todays_fixtures_info, get_tomorrows_fixtures_info, get_overtomorrows_fixtures_info, display_games_terminal, save_todays_fixture
import get_todays_fixtures

import pandas as pd
from datetime import datetime
from datetime import timedelta
# from get_todays_fixtures

class Todays_Fixtures():

    #called by controller.py to get the fixtures saved in csv file
    def get_fixtures_saved(self):
        #load the fixtures csv file
        try:
            last_saved_games = pd.read_csv(self.todays_fix_file, header = None, dtype='str')
        except:
            last_saved_games = pd.DataFrame([])     #empty dataframe
            return(last_saved_games, False)
        #add the columns
        last_saved_games.columns = ['id', 'home', 'away', 'date', 'time']
        return(last_saved_games, True)

    #called by controller.py to check if fixtures saved are from today
    def fixtures_saved(self):
        #check if fixtures saved
        last_date_saved = None
        saved_todays_fix = False
        #define todays date
        todays_date = datetime.now().day
        todays_month = datetime.now().month
        date_today = str(todays_date) + '.' + str(todays_month)

        #check if todays date is last saved date
        if (self.last_saved_games['date'][0] == date_today):
            last_date_saved = date_today
            saved_todays_fix = True
        else:
            last_date_saved = self.last_saved_games['date'][0]
            saved_todays_fix = False
        return(last_date_saved, saved_todays_fix)

        #so now we got the dataframe

    #called by controller.py to call functions in get_todays_fictures.py
    def save_fixtures_today(self):
        results_matchtoday = self.bs_bundesliga.soup.findAll("div", title='Click for match detail!')
        #each element in results_matchtoday is of type: <class 'bs4.element.Tag'>

        #MAYBE ADD THE OPTION TO HAVE THE SCORE ALREADY ON THAT PAGE (so that if we only want the score)

        ### CREATE PANDAS DATAFRAME WITH ALL FIXTURES INFO ###
        #we now send the results_matchtoday to the get_info_fixturespage and append all the data to a DF
        bundesliga_fixtures_df = get_todays_fixtures.get_info_fixturespage(results_matchtoday)
        #we get back a pandas dataframe that holds all the fixtures info on the fixtures page

        ### FILTER DATAFRAME FOR TODAYS FIXTURES ###
        #we go to the get_todays_fixtures_info function to filter the games down to the ones today
        todays_bundesliga_fixtures_df = get_todays_fixtures.get_todays_fixtures_info(bundesliga_fixtures_df)
        tomorrow_bundesliga_fixtures_df = get_todays_fixtures.get_tomorrows_fixtures_info(bundesliga_fixtures_df)
        overtomorrow_bundesliga_fixtures_df = get_todays_fixtures.get_overtomorrows_fixtures_info(bundesliga_fixtures_df)

        #To dsplay the games on terminal
        display_games = False
        if display_games:
            get_todays_fixtures.display_games_terminal(todays_bundesliga_fixtures_df, tomorrow_bundesliga_fixtures_df, overtomorrow_bundesliga_fixtures_df)

        #save to file
        saved = get_todays_fixtures.save_todays_fixture(todays_bundesliga_fixtures_df)
        if saved:
            print('saved Todays fixtures')
        else:
            print('unable to save Todays fixtures')

        if (len(todays_bundesliga_fixtures_df) < 1):
            print('No Games Today, saving empty list')
        else:
            #we return 1 to show that it was successful
            return(1)




#if running without controller.py
# if __name__ == '__main__':
#     Todays_Fixtures.fixtures_saved()

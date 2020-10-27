from controller_fixtures import Bundesliga_fixtures
from controller_game import Game_fixture

import threading
import time


if __name__ == '__main__':

    t__start = time.perf_counter()

    #league url
    url_bundesliga = "https://www.scoreboard.com/en/soccer/germany/bundesliga/fixtures/"
    url_bundesliga = "https://www.scoreboard.com/en/soccer/brazil/serie-b/fixtures/"

    ##############
    ## Need to include that it only laods the fixtures page if we dont have todays fixtures!!!
    ##############

    #now we have our object that has checked and gotten todays fixtures
    bundi_fixtures = Bundesliga_fixtures(url_bundesliga)




    # we need to detach this step so that it gets the current fixture infor seperatly and not always with the fixtures


    #now we create an object for each of the fixtures (we are interested in)
    fixtures_threads = []
    for index, row in bundi_fixtures.last_saved_games.iterrows():
        #row is not the game as a pandas Series
        game = Game_fixture(row)
        game.start_thread()
        game.game_thread.start()

        fixtures_threads.append(game.game_thread)

    for thread in fixtures_threads:
        thread.join()


    print('')
    t__done = time.perf_counter()
    t__runtime = t__done - t__start
    print('Time to run: {0}'.format(t__runtime))



    #######
    # WE NEED TO DELETE ALL THE GAME FILES
    #######

    ### add timing (beginning and end)

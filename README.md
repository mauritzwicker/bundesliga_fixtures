# bundesliga_fixtures *****WORK IN PROGRESS*****
# VERY MUCH SPAGHETTI CODE


Web scrape Bundesliga fixtures (from scoreboard.com) for score, info, lineup. Show on raspberry-pi controlled rgb-matrix.
.

Files:

get_todays_fixtures.py
#file to get the fixtures today with game-id, date, time, teams.
# TODO: need to decide how we will save this information and how to run so it runs in morning

webdriver_creater.py
#to call from other files to create the webdriver object

get_fixtures_data.py
#to get the data of a fixture off of its fixture page
# TODO: what data and how it is controlled


#for getting the list of fixtures
main.py
    --- >controller_fixtures.py
    # in here we check if we saved todays fixtures
        --> save_todays_fixtures.py
        # to save todays fixtures
    # to check if fixtures today saved and not old ones
    # if we saved old we want to save the new fixtures
        --> save_todays_fixtures.py
        # in save_fixtures_today function we get the games from the webapge
            --> get_todays_fixtures.py
            # here we just access the functions
    # now we have the newest fixtures and we recheck it and to get it in our variable

#for getting the fixtures data
main.py
#we loop and do this for every game
    --- > controller_game.py
    #we create the inidividual game object

    #we have the info in
        -> get_fixture_data.py


#to display on led matrix
display_game_led
#get the game file with the data and format the data so that we can display it on the led matrix
#this is not really working (i think we need to create a new canvas for multiple objects)


#add ons
*** now need to get more data (lineup usw)
*** now need to determine how i want to save and display the data
*** add options to search for only one specific game and so on (maybe)








### no more change needed (except __main__ or add ons)
- get_todays_fixtures.py
- controller_fixtures.py
- save_todays_fixtures.py
- webdriver_creater.py
- controller_game.py
_ get_fixtures_data.py





## need to clean up and decide how i pass variables (global vs local) (no return function)
### need to edit the if __name__ == __main__

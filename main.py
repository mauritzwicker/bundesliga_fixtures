from controller_fixtures import Bundesliga_fixtures
from controller_game import Game_fixture


if __name__ == '__main__':

    #league url
    url_bundesliga = "https://www.scoreboard.com/en/soccer/germany/bundesliga/fixtures/"

    #now we have our object that has checked and gotten todays fixtures
    bundi_fixtures = Bundesliga_fixtures(url_bundesliga)

    #now we create an object for each of the fixtures (we are interested in)
    for xx in bundi_fixtures:
        print(xx)

    #then for that fixture : fixture = Game_fixture(xx)
    #make an array of all the fixture object



####
# this is to display the game on the led
#
# input: which game we want to display (the fixture file)
# output the display on the led matrix

import time
import sys
import pandas as pd

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image
import requests
from io import BytesIO

def get_logo_image(url):
    response = requests.get(url)
    image_logo = Image.open(BytesIO(response.content))
    return(image_logo)

def display_rgb(fixture_info):

    date = fixture_info.iloc[0][0]
    goals_home = fixture_info.iloc[1][0]
    goals_away = fixture_info.iloc[2][0]
    game_status = fixture_info.iloc[3][0]
    home_team = fixture_info.iloc[4][0]
    away_team = fixture_info.iloc[5][0]
    home_img = fixture_info.iloc[6][0]
    away_img = fixture_info.iloc[7][0]

    ## now need to do stuff from try_2710.py

    ############################################################
    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

    matrix = RGBMatrix(options = options)
    ############################################################
    red = graphics.Color(255, 0, 0)

    img_width = 15
    img_height = 24

    width_scrn = matrix.width       #64
    height_scrn = matrix.height     #32

    # home team logo
    x_offset_home = 2
    y_offset_home = (height_scrn - img_height)/2
    image_home = get_logo_image(home_img)
    image_home.thumbnail((img_width, img_height), Image.ANTIALIAS)
    matrix.SetImage(image_home.convert('RGB'))

    # away team logo
    x_offset_away = width_scrn - 17
    y_offset_away = (height_scrn - img_height)/2
    image_away = get_logo_image(away_img)
    image_away.thumbnail((img_width, img_height), Image.ANTIALIAS)
    matrix.SetImage(image_away.convert('RGB'))

    fnt = ['10x20', '4x6', '5x7', '5x8', '6x10', '6x12', '6x13B', '7x13', '7x14', '7x14B', '8x13', '9x15', '9x18B', 'tom-thumb', 'texgyre-27', 'helvR12', 'clR6x12']

    font = graphics.Font()

    # score
    # font_score = "../../../fonts/clR6x12.bdf"
    # font.LoadFont(font_score)
    # score = str(home_team) + '-' + str(away_team)
    # graphics.DrawText(matrix, font, 25, (height_scrn/2) - 2, red, score)

    # # date
    # font_date = "../../../fonts/4x6.bdf"
    # font.LoadFont(font_date)
    # graphics.DrawText(matrix, font, 27, 2, red, font_date)

    # # Status
    # font_status = "../../../fonts/4x6.bdf"
    # font.LoadFont(font_status)
    # graphics.DrawText(matrix, font, 27, 2, red, game_status)

    time.sleep(5)


def read_data(path_game):
    try:
        game_information = pd.read_csv(path_game, header = None, dtype='str')
    except:
        print('failed')
    # except:
        # print('import fixture data failed')

    return(game_information)



# read the data
id_val = 'g_1_fyqLEc4e'
# path_game = './fixtures_files/fixture_' + str(id_val) + '.csv'
path_game = './fixtures_files/fixture_' + str(id_val) + '.csv'
path_game = str(path_game)
fixture_info = read_data(path_game)


display_rgb(fixture_info)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)


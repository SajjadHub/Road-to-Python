# Roku bot
from roku import Roku
import time
from datetime import date, timedelta


def playSpotify(search):
    spotify = roku['Spotify Music']
    spotify.launch()
    time.sleep(12)
    roku.select()
    time.sleep(1)
    roku.select()
    # For searching something up
    """
    roku.left()
    time.sleep(1)

    roku.down()
    time.sleep(1)

    roku.select()
    time.sleep(1)

    roku.right()
    time.sleep(1)

    roku.select()
    time.sleep(1)

    roku.literal(search)
    """


roku = Roku('192.168.0.21')

playSpotify("rap")

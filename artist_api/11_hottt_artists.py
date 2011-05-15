# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

hottt_artists = artist.top_hottt()

for hottt_artist in hottt_artists:
    print hottt_artist.name, hottt_artist.hotttnesss

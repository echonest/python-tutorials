# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song

short_quiet_songs = song.search(max_duration=90, max_loudness=-50, start=5, results=11)

if short_quiet_songs:
    for a_song in short_quiet_songs:
       print '"%s" by %s' % (a_song.title, a_song.artist_name) 
else:
    print 'No songs found.'

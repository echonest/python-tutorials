# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song
from pyechonest import artist

short_unloud_songs = song.search(max_duration=90, max_loudness=-10, start=34, results=10)

if short_unloud_songs:
    artist_ids = [a_song.artist_id for a_song in short_unloud_songs]
    artists = [artist.Artist(id) for id in set(artist_ids)]
    for an_artist in artists:
        biographies = an_artist.get_biographies(results=1)
        if biographies:
            print '%-30s %s' % (an_artist.name[0:30], biographies[0]['url'])
        else:
            print an_artist.name
else:
    print 'No songs found.'

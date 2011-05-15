# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

kc_results = artist.search(name='Kid Cudi')
if kc_results:
    kc = kc_results[0]
    for a_song in kc.get_songs(results=20, start=30):
        print '%s (Echo Nest ID: %s) by %s' % (a_song.title, a_song.id, a_song.artist_name)
else:
    print 'Artist not found.'

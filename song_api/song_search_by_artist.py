# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song

kc_songs = song.search(artist='Kid Cudi', results=20, start=30)

if kc_songs:
    for a_song in kc_songs:
       print '"%s" by %s' % (a_song.title, a_song.artist_name) 
else:
    print 'No songs found.'

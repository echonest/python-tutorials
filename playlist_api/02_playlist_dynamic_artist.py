# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import playlist

dyn_playlist = playlist.Playlist(type='artist', artist=['muse', 'death cab for cutie', 'the postal service'])

print 'First five songs in a dynamic playlist for artists Muse, Death Cab for Cutie, and The Postal Service:'
for i in range(0,5):
    print '"%s" by %s' % (dyn_playlist.song.title, dyn_playlist.song.artist_name)
    dyn_playlist.get_next_song()

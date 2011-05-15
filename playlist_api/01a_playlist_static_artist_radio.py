# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import playlist, artist

tsquare = artist.Artist('Thompson Square')
jaldean = artist.Artist('Jason Aldean')
afire = artist.Artist('Arcade Fire')

a_playlist = playlist.static(type='artist-radio', artist_id=[tsquare.id, jaldean.id, afire.id], results=5)

other_playlist = playlist.static(type='artist-radio', artist_id=[tsquare.id, jaldean.id, afire.id], results=5)

print 'Songs in one playlist for seed artists %s:' % (', '.join(an_artist.name for an_artist in [tsquare, jaldean, afire]),)
for a_song in a_playlist:
    print '"%s" by %s' % (a_song.title, a_song.artist_name)

print ''

print 'Songs in another playlist for seed artists %s:' % (', '.join(an_artist.name for an_artist in [tsquare, jaldean, afire]),)
for a_song in other_playlist:
    print '"%s" by %s' % (a_song.title, a_song.artist_name)

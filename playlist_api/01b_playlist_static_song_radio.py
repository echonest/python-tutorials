# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import playlist, song

kwstr = song.Song('SOSGSJB12A8C13B2D4')
dptec = song.Song('SOOSADY12A6701F119')
jwcb = song.Song('SOCEGKM12A58A7F30D')

a_playlist = playlist.static(type='song-radio', song_id=[kwstr.id, dptec.id, jwcb.id], results=5)

other_playlist = playlist.static(type='song-radio', song_id=[kwstr.id, dptec.id, jwcb.id], results=5)

print 'Songs in one playlist for seed songs "%s":' % ('," "'.join(a_song.title for a_song in [kwstr, dptec, jwcb]),)
for a_song in a_playlist:
    print '"%s" by %s' % (a_song.title, a_song.artist_name)

print ''

print 'Songs in another playlist for seed songs "%s":' % ('," "'.join(a_song.title for a_song in [kwstr, dptec, jwcb]),)
for a_song in other_playlist:
    print '"%s" by %s' % (a_song.title, a_song.artist_name)

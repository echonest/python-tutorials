# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song

ntt_results = song.search(artist='Charlie Parker', title='Now\'s the time')
ritd_results = song.search(artist='Adele', title='rolling in the deep')

if ntt_results and ritd_results:
    for a_song in [ntt_results[0], ritd_results[0]]:
        print '"%s" (%s)\nby %s (%s)' % (a_song.title, a_song.id, a_song.artist_name, a_song.artist_id)
        print 'Song hotttnesss: ', a_song.song_hotttnesss
        print 'Artist hotttnesss: %s, artist familiarity: %s' % (a_song.artist_hotttnesss, a_song.artist_familiarity)
        print 'Artist location:'
        for loc_key, loc_val in a_song.artist_location.iteritems():
            print '    %-13s %s' % (loc_key, loc_val)
        print ''
else:
    print 'Missing a song.'

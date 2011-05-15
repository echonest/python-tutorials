# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song

groovy_results = song.search(title='59th Street Bridge Song', artist='Simon & Garfunkel', buckets=['id:7digital'], limit=True)

if groovy_results:
    groovy = groovy_results[1]
    print 'Tracks for "%s" (%s)\nby %s (%s):\n' % (groovy.title, groovy.id, groovy.artist_name, groovy.artist_id)
    for a_track in groovy.get_tracks('7digital'):
        print 'Track ID: %s' % (a_track['id'])
        for key, val in a_track.iteritems():
            print '    %-20s %s' % (key, val)
        print ''
else:
    print 'No songs found.'

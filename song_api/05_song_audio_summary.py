# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song

ts_results = song.search(artist='the beatles', title='twist and shout')

if ts_results:
    ts = ts_results[0]
    print 'Audio summary of "%s" by %s:' % (ts.title,ts.artist_name)
    for aud_key, aud_val in ts.audio_summary.iteritems():
        print '    %-15s %s' % (aud_key, aud_val)
else:
    print 'No songs found.'

# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

weezer_results = artist.search(name='weezer')

if weezer_results:
    weezer = weezer_results[0]
    print 'Biographies for %s:' % (weezer.name,)
    for bio_document in weezer.biographies:
        print '%s' % (bio_document['site'],)
        for key, val in bio_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

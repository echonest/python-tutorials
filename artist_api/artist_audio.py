# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

be_results = artist.search(name='bright eyes')

if be_results:
    be = be_results[0]
    print 'Audio for %s:' % (be.name,)
    for audio_document in be.audio:
        print '%s' % (audio_document['artist'],)
        for key, val in audio_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

okg_results = artist.search(name='OK Go')

if okg_results:
    okg = okg_results[0]
    print 'Vidoes for %s:' % (okg.name,)
    for video_document in okg.video:
        print '%s' % (video_document['title'])
        for key, val in video_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

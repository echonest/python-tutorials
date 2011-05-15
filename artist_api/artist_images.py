# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

td_results = artist.search(name='The Decemberists')

if td_results:
    td = td_results[0]
    print 'Images for %s:' % (td.name,)
    for image_document in td.images:
        print '%s' % (image_document['url'][image_document['url'].rfind('/') + 1:],)
        for key, val in image_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

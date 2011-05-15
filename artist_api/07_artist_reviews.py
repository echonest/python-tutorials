# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

td_results = artist.search(name='The Decemberists')

if td_results:
    td = td_results[0]
    for review_document in td.reviews:
        print 'Album Review: "%s" by %s' % (review_document['release'], td.name)
        for key, val in review_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

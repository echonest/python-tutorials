# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

bk_results = artist.search(name='bikini kill')

if bk_results:
    bk = bk_results[0]
    print 'News for %s:' % (bk.name,)
    for news_document in bk.news:
        print '%s' % (news_document['name'],)
        for key, val in news_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

weezer_results = artist.search(name='weezer')

if weezer_results:
    weezer = weezer_results[0]
    print 'Blogs for %s:' % (weezer.name,)
    for blog_document in weezer.blogs:
        print '%s' % (blog_document['name'],)
        for key, val in blog_document.iteritems():
            print '    \'%s\': %s' % (key, val)
else:
    print 'Artist not found.'

# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

okg_results = artist.search(name='OK Go')

if okg_results:
    okg = okg_results[0]
    print '%s (Echo Nest Artist ID: %s)' % (okg.name, okg.id)
    print 'Hotttnesss: %s, Familiarity: %s\n' % (okg.hotttnesss, okg.familiarity)
    print 'Terms: ', ', '.join([term.get('name') for term in okg.terms]), '\n'
    print 'Similar artists: ', ', '.join(similar_artist.name for similar_artist in okg.similar), '\n' 

    print 'Artist URLs:'
    for url_key, url_val in okg.urls.iteritems():
        print '%-16s %s' % ('\'' + url_key + '\'' + ':', url_val)

    print '\n%-20s %s' % ('News articles found:', okg.news.total)
    print '%-20s %s' % ('Blog articles found:', okg.blogs.total)
    print '%-20s %s' % ('Album reviews found:', okg.reviews.total)
    print '%-20s %s' % ('Songs found:', okg.songs.total)
    print '%-20s %s' % ('Audio URLs found:', okg.audio.total)
    print '%-20s %s' % ('Videos found:', okg.video.total)
    print '%-20s %s' % ('Images found:', okg.images.total)
    print '%-20s %s' % ('Biographies found:', okg.biographies.total)
else:
    print 'Artist not found.'

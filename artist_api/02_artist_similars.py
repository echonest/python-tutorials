# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

bk_results = artist.search(name='bikini kill')

if bk_results:
    bk = bk_results[0]
    print 'Artists similar to: %s:' % (bk.name,)
    for similar_artist in bk.similar:
        print '    %s' % (similar_artist.name,)
else:
    print 'Artist not found.'

# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

ra_search_results = artist.search(name='Rise Against')
if ra_search_results:
    ra_by_search = ra_search_results[0]

    print 'Found "%s" (%s) by artist.search()' % (ra_by_search.name, ra_by_search.id)

    ra_by_id = artist.Artist('ARZWK2R1187B98F09F')

    if (ra_by_id == ra_by_search):
        print 'Found "%s" (%s) by ID initialization' % (ra_by_id.name, ra_by_id.id)

    ra_by_name = artist.Artist('Rise Against')

    if (ra_by_name == ra_by_search):
        print 'Found "%s" (%s) by name initialization' % (ra_by_name.name, ra_by_name.id)

else:
    print 'Artist not found by artist.search()'

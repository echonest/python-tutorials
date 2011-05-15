# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

buckets_options = [['id:7digital'],
                   ['id:playme'], 
                   ['id:musicbrainz'], 
                   ['id:7digital', 'id:playme', 'id:musicbrainz']]

for bucket_set in buckets_options: 
    te_results = artist.search(name='The Ernies', buckets=bucket_set, limit=True)
    if te_results:
        print 'Found %s in %s.' % (te_results[0].name, bucket_set)
    else:
        print 'Not found in %s.' % (bucket_set,)

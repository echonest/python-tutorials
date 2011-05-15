# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

hottt_artists = artist.top_hottt(results=3)

similar_artists = artist.similar(names=[hottt_artist.name for hottt_artist in hottt_artists])

for similar_artist in similar_artists:
    similar_to = [] 
    for hottt_artist in hottt_artists:
        if similar_artist in hottt_artist.similar:
            similar_to.append(hottt_artist.name)

    print '%-30s %16s   %s' % (similar_artist.name[0:30], 
                               similar_artist.hotttnesss, 
                               '...is in the top 15 similars of: ' + ', '.join(similar_to))

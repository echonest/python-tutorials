# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import artist

synthpop_results = artist.search(description=['synthpop'], buckets=['id:7digital', 'id:musicbrainz'], results=5)

for sp_artist in synthpop_results:
    print '%s (Echonest Nest ID: %s)' % (sp_artist.name, sp_artist.id)
    temp_artist = artist.Artist(sp_artist.get_foreign_id('7digital'))
    if temp_artist == sp_artist:
        print '%s (Echonest Nest ID: %s)' % (temp_artist.name, temp_artist.id)
    else:
        print '7digital artist is not the same'

    print '    7digitial ID: ', sp_artist.get_foreign_id('7digital')
    print '    MusicBrainz ID: ', sp_artist.get_foreign_id('musicbrainz'), '\n'

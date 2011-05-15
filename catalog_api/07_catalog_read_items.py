# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import catalog

c = catalog.Catalog('example_songs', type='song')

for item in c.read_items(buckets=['audio_summary','artist_hotttnesss']):
    print '"%s"' % (item.title,)
    print '    artist_hotttness: %s' % (item.artist_hotttnesss)
    print '    tempo: %s' % (item.audio_summary['tempo'])
    print '    energy: %s' % (item.audio_summary['energy'])

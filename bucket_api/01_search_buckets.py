# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song
from pyechonest import artist

jazzy_results = artist.search(description=['jazz', 'bebop'], buckets=['hotttnesss', 'images'], results=5)

for jazzy_artist in jazzy_results:
    print jazzy_artist.name
    print 'hotttnesss: ', jazzy_artist.hotttnesss
    if jazzy_artist.images:
        print 'image: ', jazzy_artist.images[0]['url']

    print 'songs:'
    ja_songs = song.search(artist_id=jazzy_artist.id, buckets=['audio_summary'], results=3)
    for ja_song in ja_songs:
        print '    "%s"\n        tempo: %s, energy: %s' % (ja_song.title, ja_song.audio_summary['tempo'], ja_song.audio_summary['energy'])

    print ''
